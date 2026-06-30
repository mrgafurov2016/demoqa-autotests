import pytest


def test_get_all_books_returns_list(api_client):
    response = api_client.get_all_books()

    assert response.status_code == 200
    books = response.json()["books"]
    assert len(books) > 0


def test_create_user_success(api_client):
    import uuid
    username = f"user_{uuid.uuid4().hex[:10]}"

    response = api_client.create_user(username, "Gafurov123!")

    assert response.status_code == 201
    assert response.json()["username"] == username


def test_create_user_with_weak_password_fails(api_client):
    import uuid
    username = f"user_{uuid.uuid4().hex[:10]}"

    response = api_client.create_user(username, "weak")

    assert response.status_code == 400


def test_generate_token_for_registered_user(registered_user, api_client):
    response = api_client.generate_token(
        registered_user["username"], registered_user["password"]
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Success"


def test_add_book_to_user(registered_user, api_client):
    isbn = "9781449325862"

    response = api_client.add_book_to_user(
        registered_user["user_id"], isbn, registered_user["token"]
    )

    assert response.status_code == 201
    added_isbns = [book["isbn"] for book in response.json()["books"]]
    assert isbn in added_isbns


def test_delete_book_from_user(registered_user, api_client):
    isbn = "9781449325862"
    api_client.add_book_to_user(registered_user["user_id"], isbn, registered_user["token"])

    response = api_client.delete_book(isbn, registered_user["user_id"], registered_user["token"])

    assert response.status_code == 204