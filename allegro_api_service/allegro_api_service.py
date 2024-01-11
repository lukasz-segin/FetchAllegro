import json

import requests

from allegro_api_client.allegro_api_client import AllegroApiClient
from fetch_allegro.settings import Settings

"""
Service for calling the Allegro API
"""


class AllegroApiService:
    def __init__(self):
        self._settings = Settings()
        self._api_client = AllegroApiClient(
            allegro_client_id=self._settings.CLIENT_ID,
            allegro_client_secret=self._settings.CLIENT_SECRET,
            allegro_token_url=self._settings.TOKEN_URL,
        )

    def get_access_token(self):
        try:
            data = {"grant_type": "client_credentials"}
            access_token_response = requests.post(
                self._settings.TOKEN_URL,
                data=data,
                verify=False,
                allow_redirects=False,
                auth=(self._settings.CLIENT_ID, self._settings.CLIENT_SECRET),
            )
            tokens = json.loads(access_token_response.text)
            access_token = tokens["access_token"]
            return access_token
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    def get_main_categories(self, token):
        try:
            headers = {"Authorization": "Bearer " + token, "Accept": "application/vnd.allegro.public.v1+json"}
            main_categories_result = requests.get(
                self._settings.SALE_CATEGORIES_URL, headers=headers, verify=False
            )
            return main_categories_result
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
