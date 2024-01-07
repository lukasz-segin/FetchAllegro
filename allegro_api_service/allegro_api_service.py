import os

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
            access_token_response = requests.post(self.api_client.allegro_token_url, data=data, verify=False,
                                                  allow_redirects=False,
                                                  auth=(self.api_client.allegro_client_id,
                                                        self.api_client.allegro_client_secret))
            tokens = json.loads(access_token_response.text)
            access_token = tokens['access_token']
            return access_token
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
