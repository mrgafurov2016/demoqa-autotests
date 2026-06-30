import pytest
from selenium import webdriver
import uuid
from api.bookstore_client import BookstoreClient


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  # включишь позже для CI

    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture
def api_client():
    return BookstoreClient()


@pytest.fixture
def registered_user(api_client):
    username = f"user_{uuid.uuid4().hex[:10]}"
    password = "Gafurov123!"

    create_response = api_client.create_user(username, password)
    user_id = create_response.json()["userID"]

    token_response = api_client.generate_token(username, password)
    token = token_response.json()["token"]

    return {
        "username": username,
        "password": password,
        "user_id": user_id,
        "token": token,
    }