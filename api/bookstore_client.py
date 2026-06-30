import requests


class BookstoreClient:
    BASE_URL = "https://demoqa.com"

    def __init__(self):
        self.session = requests.Session()

    def create_user(self, username, password):
        url = f"{self.BASE_URL}/Account/v1/User"
        payload = {"userName": username, "password": password}
        return self.session.post(url, json=payload)

    def generate_token(self, username, password):
        url = f"{self.BASE_URL}/Account/v1/GenerateToken"
        payload = {"userName": username, "password": password}
        return self.session.post(url, json=payload)

    def get_all_books(self):
        url = f"{self.BASE_URL}/BookStore/v1/Books"
        return self.session.get(url)

    def add_book_to_user(self, user_id, isbn, token):
        url = f"{self.BASE_URL}/BookStore/v1/Books"
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"userId": user_id, "collectionOfIsbns": [{"isbn": isbn}]}
        return self.session.post(url, json=payload, headers=headers)

    def delete_book(self, isbn, user_id, token):
        url = f"{self.BASE_URL}/BookStore/v1/Book"
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"isbn": isbn, "userId": user_id}
        return self.session.delete(url, json=payload, headers=headers)