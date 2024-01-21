import requests

from fetch_allegro.settings import Settings


class AllegroApiService:
    def __init__(self, api_client):
        self._api_client = api_client

    def get_access_token(self):
        try:
            data = {"grant_type": "client_credentials"}
            response = requests.post(
                self._api_client.allegro_token_url,
                data=data,
                auth=(self._api_client.allegro_client_id, self._api_client.allegro_client_secret),
            )
            response.raise_for_status()
            tokens = response.json()
            return tokens["access_token"]
        except requests.RequestException as err:
            print(f"Authentication failed: {err}")
            return None

    @staticmethod
    def _api_request(endpoint, headers):
        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as err:
            print(f"API request failed: {err}")
            return None

    def get_main_categories(self, token):
        headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.allegro.public.v1+json"}
        return self._api_request(Settings().ALLEGRO_SALE_CATEGORIES_URL, headers)
