from collections import defaultdict

from flask import Flask, request, jsonify

app = Flask(__name__)

# Error message
err_string = """Your request must include data formated as:
        {
        "productListings": [{"productID": "123", "authorizedSellerID": "A1"}],
        "salesTransactions": [{"productID": "123", "sellerID": "B2"}]
        }"""


@app.route('/', methods=['POST'])
def check_unauthorized_sales():
    if 'productListings' not in request.json or 'salesTransactions' not in request.json:
        return jsonify({"error": err_string}), 400

    data = request.json
    product_listings = data['productListings']
    sales_transactions = data['salesTransactions']

    unauthorized_sales = []

    # Create a dictionary to quickly lookup authorized sellers by productID
    authorized_sellers_dict = defaultdict(list)
    for listing in product_listings:
        authorized_sellers_dict[listing['productID']].append(listing['authorizedSellerID'])

    for transaction in sales_transactions:
        product_id = transaction['productID']
        seller_id = transaction['sellerID']

        # If productID is not found in product_listings or sellerID not in authorized_sellers
        if product_id not in authorized_sellers_dict or seller_id not in authorized_sellers_dict[product_id]:
            unauthorized_sales.append({"productID": product_id, "unauthorizedSellerID": [seller_id]})

    if len(unauthorized_sales) == 0:
        return jsonify({"unauthorizedSales": "No unauthorized sales!"}), 200
    return jsonify({"unauthorizedSales": unauthorized_sales}), 200


if __name__ == '__main__':
    app.run()
