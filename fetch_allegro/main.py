# from flask import Flask, request, jsonify
import os

from allegro_api_service.allegro_api_service import AllegroApiService

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
    print("Fetching allegro categories")
    service = AllegroApiService()
    token = service.get_access_token()
    categories = service.get_main_categories(token)
    print(categories.json())
