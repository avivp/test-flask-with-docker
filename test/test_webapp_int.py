import pytest
import docker
import requests

@pytest.fixture
def generate_container(autouse=True, scope="module"):    # all tests automatically request this fixture
    client = docker.from_env()
    container = client.containers.run("test1", ports={'5000/tcp': 5000}, detach=True)
    #  using yield the code block after the yield statement is executed as teardown code regardless of the test outcome, and must yield exactly once.
    yield container
    container.stop()


def test_webapp(generate_container):
  
    # r = requests.get('http://127.0.0.1:5000/')
    # print(r.status_code)
    r = requests.get('http://127.0.0.1:5000/item/1')
    assert r.json().name == "item1"
