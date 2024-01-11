"""
Client for communicating with the Allegro API

Args:
    allegro_client_id: The Allegro client ID
    allegro_client_secret: The Allegro client secret
    allegro_token_url: The Allegro token URL
"""


class AllegroApiClient:
    def __init__(self, allegro_client_id: str, allegro_client_secret: str, allegro_token_url: str):
        self.allegro_client_id = allegro_client_id
        self.allegro_client_secret = allegro_client_secret
        self.allegro_token_url = allegro_token_url
