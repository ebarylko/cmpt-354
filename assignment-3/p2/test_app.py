from app import app
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
def test_trade(path, expected):
    client = app.test_client()
    response = client.get(path).text
    assert expected in response
