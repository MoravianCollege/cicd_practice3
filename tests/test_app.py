from practice.app import app


def test_get_page():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/practice')
    assert b'Hello world!' in result.data