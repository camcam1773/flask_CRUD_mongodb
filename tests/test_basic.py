def test_basic(client):
    response = client.get('/')
    assert b'Basic CRUD App with Python Flask' in response.data
    assert b"Nothing yet..." in response.data
    assert b'Delete' not in response.data
    assert b'Update' not in response.data


def poster(client, content: str):
    return client.post('/', data=dict(content=content), follow_redirects=True)


def test_create_task(client):
    response = poster(client, "Yolo")
    assert response.status_code == 200
    response = client.get('/')
    assert b"Yolo" in response.data
