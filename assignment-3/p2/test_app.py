from app import app
import pytest

# client = app.test_client()
@pytest.mark.parametrize("path, expected", [("/getOwner?aid=800", "800"),
                                            ("/getOwner?aid=150", '{"150":1001001000},'
                                                                  '{"150":5005005000}'),
                                            ("/getOwner?aid=1000", "-1")])
def test_getOwner(path, expected):
    client = app.test_client()
    response = client.get(path).text
    assert expected in response

