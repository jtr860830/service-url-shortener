from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.database import Base, engine

client = TestClient(app)

username: str = "user"
password: str = "pass"
token: str
original: str = "https://www.google.com"
update_original: str = "https://github.com"
alias: str


@pytest.fixture(scope="module", autouse=True)
def before_all_after_all():
    # before all test start
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # after all test finish
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_create_user():
    data: dict = {"username": username, "password": password}
    headers: dict = {"Content-Type": "application/json"}
    res = client.post("/users/", json=data, headers=headers)
    assert res.status_code == 201
    assert res.json().get("data").get("username") == username


def test_create_token():
    data: dict = {"username": username, "password": password}
    headers: dict = {"Content-Type": "application/json"}
    res = client.post("/tokens/", json=data, headers=headers)
    global token
    token = res.json().get("data").get("access_token")
    assert res.status_code == 201
    assert res.json().get("data").get("token_type") == "Bearer"
    assert isinstance(token, str)


def test_get_user():
    global token
    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    res = client.get("/users/me", headers=headers)
    assert res.status_code == 200
    assert res.json().get("data").get("username") == username


def test_create_url():
    data: dict = {"original": original}
    global token
    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    res = client.post("/urls/", json=data, headers=headers)
    global alias
    alias = res.json().get("data").get("alias")
    assert res.status_code == 201
    assert res.json().get("data").get("original") == original
    assert isinstance(alias, str)


def test_get_all_urls():
    global token
    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    res = client.get("/urls/", headers=headers)
    assert res.status_code == 200
    assert res.json().get("data")[0].get("original") == original
    global alias
    assert res.json().get("data")[0].get("alias") == alias


def test_redirect_url():
    global token
    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    global alias
    res = client.get(f"/urls/{alias}", headers=headers, allow_redirects=False)
    assert res.status_code == 307


def test_update_url():
    data: dict = {"original": update_original}
    global token
    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    global alias
    res = client.patch(f"/urls/{alias}", json=data, headers=headers)
    assert res.status_code == 200
    assert res.json().get("data").get("alias") == alias
    assert res.json().get("data").get("original") == update_original


def test_delete_url():
    global token
    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    global alias
    res = client.delete(f"/urls/{alias}", headers=headers)
    assert res.status_code == 204
