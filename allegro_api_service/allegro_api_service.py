import json
import os
import requests

from allegro_api_client.allegro_api_client import AllegroApiClient

"""
Service for calling the Allegro API
"""

allegro_api = AllegroApiClient(allegro_client_id=os.getenv('CLIENT_ID'),
                               allegro_client_secret=os.getenv('CLIENT_SECRET'),
                               allegro_token_url=os.getenv('TOKEN_URL'))


class AllegroApiService:
    def __init__(self):
        self.api_client: AllegroApiClient = allegro_api

    def get_access_token(self):
        try:
            data = {'grant_type': 'client_credentials'}
            access_token_response = requests.post(os.getenv('TOKEN_URL'), data=data, verify=False,
                                                  allow_redirects=False,
                                                  auth=(os.getenv('CLIENT_ID'),
                                                        os.getenv('CLIENT_SECRET')))
            tokens = json.loads(access_token_response.text)
            access_token = tokens['access_token']
            return access_token
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    @staticmethod
    def get_main_categories(token):
        try:
            headers = {'Authorization': 'Bearer ' + token, 'Accept': "application/vnd.allegro.public.v1+json"}
            main_categories_result = requests.get(os.getenv('SALE_CATEGORIES_URL'), headers=headers, verify=False)
            return main_categories_result
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
