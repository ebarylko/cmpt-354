-- Write an INSERT statement on Account that fails because the
-- account's brokerpid doesn't refer to an existing broker.
Insert into Account values (120, 1001001000)


Insert into Account values (120, 1001001000)

DELETE from Broker where pid = 4004004000

INSERT into Trade VALUES (100, 4, 'err', '2024-01-31 13:00:00', 'AAPL', 6.00, 143.68);

DELETE from Trade where aid = 100;

INSERT into Trade Values (100, 0, 'buy', '2024-01-31 13:00:00', 'AAPL', 6.00, 143.68);

UPDATE Broker set pid = 1001001000 where pid = 2002002000;

INSERT into Trade values (100, 4, 'sell', '2024-01-31 13:00:00', 'AAPL', 11, 143.68);
INSERT into Trade values (100, 1, 'sell', '2029-08-31 13:00:00', 'XOM', 11, 143.68);
