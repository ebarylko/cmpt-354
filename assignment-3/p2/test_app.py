from app import app, db
from sqlalchemy import text
import pytest


@pytest.mark.parametrize("path, expected", [("/getOwner?aid=800", "800"),
                                            ("/getOwner?aid=150", '{"pid":1001001000},{"pid":5005005000}'),
                                            ("/getOwner?aid=1000", "-1")])
def test_getOwner(path, expected):
    client = app.test_client()
    response = client.get(path).text
    assert expected in response


@pytest.mark.parametrize("path, expected", [("/getHoldings?aid=150&sym=AAPL", "4.00"),
                                            ("/getHoldings?aid=1000&sym=AAPL", "-1"),
                                            ("/getHoldings?aid=150&sym=se", "-1"),
                                            ("/getHoldings?aid=800&sym=AAPL", "0")])
def test_getHoldings(path, expected):
    client = app.test_client()
    response = client.get(path).text
    assert expected in response


@pytest.mark.parametrize("path, expected", [("/trade?aid=300&sym=GOOGL&type=buy&shares=100.00&price=99.99", "2"),
                                            ("/trade?aid=138&sym=AAPL&type=sell&shares=101.00&price=200.20", "fail"),
                                            ("/trade?aid=188&sym=AAPL&type=buy&shares=101.00&price=200.20", "fail"),
                                            ("/trade?aid=138&sym=A&type=buy&shares=101.00&price=200.20", "fail")])
def test_trade_response(path, expected):
    client = app.test_client()
    response = client.get(path).text
    assert expected in response


@pytest.mark.parametrize('path, expected_values, pred', [("/trade?aid=300&sym=GOOGL&type=buy&shares=100.00&price=99.99", (300, 'GOOGL', 'buy', 100.00, 99.99, 2), "exists"),
                                                         ("/trade?aid=138&sym=APPL&type=sell&shares=101.00&price=200.20", (138, 'APPL', 'sell', 101.00, 200.20, 5), "not exists"),
                                                         ("/trade?aid=800&sym=GOOGL&type=sell&shares=4.00&price=200.20", (800, 'GOOGL', 'sell', 4, 200.20, 3), "not exists")
                                                         ])
def test_table_state_after_trade(path, expected_values, pred):
    client = app.test_client()
    expected_aid, expected_sym, expected_type, expected_shares, expected_price, expected_trade_seq = expected_values
    new_trade_query = text("select {pred}(select * from trade where aid=:aid and sym=:sym and type=:type and shares=:shares and seq=:trade_id and price=:price)".
                           format(pred=pred))
    client.get(path)
    with app.app_context():
        res = db.session.execute(new_trade_query, {"aid": expected_aid,
                                                   "sym": expected_sym,
                                                   "type": expected_type,
                                                   "shares": expected_shares,
                                                   "trade_id": expected_trade_seq,
                                                   "price": expected_price
                                                   }).all()
        assert res
        db.session.rollback()