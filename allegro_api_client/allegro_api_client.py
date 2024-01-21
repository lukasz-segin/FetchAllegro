class AllegroApiClient:
    """
    Client for communicating with the Allegro API

    Args:
        allegro_client_id (str): The Allegro client ID
        allegro_client_secret (str): The Allegro client secret
        allegro_token_url (str): The Allegro token URL
    """

    def __init__(self, allegro_client_id: str, allegro_client_secret: str, allegro_token_url: str) -> None:
        """
        Initializes the AllegroApiClient with the provided credentials.

        Args:
            allegro_client_id (str): The Allegro client ID
            allegro_client_secret (str): The Allegro client secret
            allegro_token_url (str): The Allegro token URL
        """
        self.allegro_client_id = allegro_client_id
        self.allegro_client_secret = allegro_client_secret
        self.allegro_token_url = allegro_token_url
