# from flask import Flask, request, jsonify
import os

from allegro_api_client.allegro_api_client import AllegroApiClient
from allegro_api_service.allegro_api_service import AllegroApiService
from fetch_allegro.settings import Settings

# app = Flask(__name__)
#
# @app.route('/offers', methods=['GET'])
# def get_offers():
#     # Get the search query from the request.
#     query = request.args.get('q')
#
#     # Call the Allegro API to fetch the offers.
#     offers = allegro_api.get_offers(query)
#
#     # Return the results as JSON.
#     return jsonify(offers)

if __name__ == "__main__":
    # app.run()

    # Initialize AllegroApiClient
    allegro_client = AllegroApiClient(
        allegro_client_id=Settings().ALLEGRO_CLIENT_ID,
        allegro_client_secret=Settings().ALLEGRO_CLIENT_SECRET,
        allegro_token_url=Settings().ALLEGRO_TOKEN_URL,
    )

    # Initialize AllegroApiService with the pre-initialized AllegroApiClient
    allegro_service = AllegroApiService(api_client=allegro_client)

    token = allegro_service.get_access_token()
    print("Fetching allegro categories")
    categories = allegro_service.get_main_categories(token=token)
    print(categories.json())

    print("Fetching allegro products (first page)")
    products = allegro_service.get_products(token=token, product_name="iphone")
    print(products.json())
