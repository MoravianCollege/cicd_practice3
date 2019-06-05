from practice.app import app


def test_get_hello():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/hello')
    assert b'Hello world!' in result.data