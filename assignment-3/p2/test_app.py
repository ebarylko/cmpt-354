from app import app, db
from sqlalchemy import text
import pytest


@pytest.mark.parametrize("path, expected", [("/getOwner?aid=800", "800"),
                                            ("/getOwner?aid=150", '{"pid":1001001000},'
                                                                  '{"pid":5005005000}'),
                                            ("/getOwner?aid=1000", "-1")])
def test_getOwner(path, expected):
    client = app.test_client()
    response = client.get(path).text
    assert expected in response


@pytest.mark.parametrize("path, expected", [("/getHoldings?aid=150&sym=AAPL", "4.00"),
                                            ("/getHoldings?aid=1000&sym=AAPL", "-1"),
                                            ("/getHoldings?aid=800&sym=AAPL", "0")])
def test_getHoldings(path, expected):
    client = app.test_client()
    response = client.get(path).text
    assert expected in response


@pytest.mark.parametrize("path, expected", [("/trade?aid=300&sym=GOOGL&type=buy&shares=100.00&price=99.99", "2"),
                                            ("/trade?aid=138&sym=AAPL&type=sell&shares=101.00&price=200.20", "fail")])
def test_trade_response(path, expected):
    client = app.test_client()
    response = client.get(path).text
    assert expected in response


@pytest.mark.parametrize('path, expected_values, pred', [("/trade?aid=300&sym=GOOGL&type=buy&shares=100.00&price=99.99", (300, 'GOOGL', 'buy', 100, 99.99, 2), "exists"),
                                                         ("/trade?aid=138&sym=AAPL&type=sell&shares=101.00&price=200.20", (138, 'AAPL', 'sell', 101, 200.20, 5), "not exists")])
def test_table_state_after_trade(path, expected_values, pred):
    with app.test_client() as client:
        client.get(path)
        expected_aid, expected_sym, expected_type, expected_shares, expected_price, expected_trade_seq = expected_values
        new_trade_query = text("select {pred}(select * from trade where aid=:aid and sym=:sym and type=:type and shares=:shares and seq=:trade_id and price=:price)".format(pred=pred))

        return db.session.execute(new_trade_query, {"pred": pred,
                                                    "aid": expected_aid,
                                                    "sym": expected_sym,
                                                    "type": expected_type,
                                                    "shares": expected_shares,
                                                    "trade_id": expected_trade_seq,
                                                    "price": expected_price}).scalar()
