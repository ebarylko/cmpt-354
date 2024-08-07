----------------------------------------------------------------------
-- (a) is enforced by CREATE TABLE statements 
-- (b) Modify the CREATE TABLE statements as needed to add
-- constraints.  Do not otherwise change the column names or types.

CREATE TABLE Person
(pid DECIMAL(10,0) NOT NULL PRIMARY KEY,
 name VARCHAR(256) NOT NULL,
 address VARCHAR(256) NOT NULL);

CREATE TABLE Broker
(pid DECIMAL(10,0) NOT NULL PRIMARY KEY REFERENCES Person(pid),
 license VARCHAR(20) NOT NULL UNIQUE,
 phone DECIMAL(10,0) NOT NULL,
 manager DECIMAL(10,0) REFERENCES Broker(pid));

CREATE TABLE Account
(aid INTEGER NOT NULL PRIMARY KEY,
 brokerpid DECIMAL(10,0) NOT NULL REFERENCES Broker(pid));

CREATE TABLE Owns
(pid DECIMAL(10,0) NOT NULL REFERENCES Person(pid),
 aid INTEGER NOT NULL REFERENCES Account(aid),
 PRIMARY KEY (pid, aid));

CREATE TABLE Stock
(sym CHAR(5) NOT NULL PRIMARY KEY,
 price DECIMAL(10,2) NOT NULL);

CREATE TABLE Trade
(aid INTEGER NOT NULL REFERENCES Account(aid),
 seq INTEGER NOT NULL,
 type CHAR(4) NOT NULL check (type in ('buy', 'sell')),
 timestamp TIMESTAMP NOT NULL,
 sym CHAR(5) NOT NULL REFERENCES Stock(sym),
 shares DECIMAL(10,2) NOT NULL,
 price DECIMAL(10,2) NOT NULL,
 PRIMARY KEY (aid, seq));

----------------------------------------------------------------------
-- (c) There is no room for mistakes at PITS. Since PITS records only
-- completed trades, enforce that the Trade table is append-only
-- (i.e., no DELETE or UPDATE is allowed) using a trigger. Further
-- enforce that within each account, trades must be recorded
-- sequentially over time: i.e., compared with old trades in the same
-- account, a new trade must have a seq that is strictly larger, and a
-- timestamp that is no less than the old values.

CREATE FUNCTION TF_TradeSeqAppendOnly() RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP IN ('DELETE', 'UPDATE') THEN
    RAISE EXCEPTION 'trade table is append-only';
  END IF;
  IF new.seq < ANY(select seq from Trade T where T.aid = new.aid) THEN
      RAISE EXCEPTION  'New trade cannot use an old trade id';
  end if;
  IF new.timestamp < ANY(select timestamp from Trade T where T.aid = new.aid) THEN
      RAISE exception 'New trade cannot occur before the previous latest trade';
  end if;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER TG_TradeSeqAppendOnly
  BEFORE INSERT OR UPDATE OR DELETE ON Trade
  FOR EACH ROW
  EXECUTE PROCEDURE TF_TradeSeqAppendOnly();

----------------------------------------------------------------------
-- (d) Using triggers, enforce that brokers cannot own accounts,
-- either by themselves or jointly with others.

CREATE FUNCTION TF_BrokerNotAccountOwner() RETURNS TRIGGER AS $$
BEGIN

    if tg_table_name = 'broker' and new.pid in (select pid from owns)
        or tg_table_name = 'owns' and new.pid in (select pid from broker) THEN
        raise exception 'A broker can not own an account';
    end if;

--     if tg_table_name = 'broker' and new.pid in (select pid from owns)THEN
--             raise exception 'A broker can not own an account';
--     end if;
--
--     if tg_table_name = 'owns' and new.pid in (select pid from broker) THEN
--             raise exception 'A broker can not own an account';
--     end if;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER TG_BrokerNotAccountOwner_Broker
  BEFORE INSERT OR UPDATE OF pid ON Broker
  -- note that DELETE won't cause a violation
  FOR EACH ROW
  EXECUTE PROCEDURE TF_BrokerNotAccountOwner();

CREATE TRIGGER TG_BrokerNotAccountOwner_Owns
  BEFORE INSERT OR UPDATE OF pid ON Owns
  -- note that DELETE won't cause a violation
  FOR EACH ROW
  EXECUTE PROCEDURE TF_BrokerNotAccountOwner();

----------------------------------------------------------------------
-- (e) Define a view Holds (aid, sym, amount) that returns the current
-- account holdings, computed from the Trade table. You may assume
-- that all accounts start with holding nothing and all transactions
-- are recorded in Trade.
CREATE VIEW Holds(aid, sym, shares) AS
select aid, sym, sum(case when type = 'buy' then shares else shares * -1 end) as shares
from trade
group by sym, aid;


CREATE FUNCTION TF_NoOverSell() RETURNS TRIGGER AS $$
BEGIN
  IF NEW.type = 'sell' AND
     NEW.shares > COALESCE((SELECT shares FROM Holds WHERE aid = NEW.aid AND sym = NEW.sym), 0) THEN
    RAISE EXCEPTION 'cannot sell more than the number of % shares currently held',
                    NEW.sym;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER TG_NoOverSell
  BEFORE INSERT ON Trade
  FOR EACH ROW
  EXECUTE PROCEDURE TF_NoOverSell();
