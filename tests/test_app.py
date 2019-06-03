from cicd.app import app


def test_get_practice():
    app.config['TESTING'] = True
    client = app.test_client()


    result = client.get('/practice')
    assert b'Hello world!' in result.data