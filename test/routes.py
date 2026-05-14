@app.route("/products/<int:product_id>", methods=["GET"])
def get_products(product_id):
    """
    Retrieve a single Product
    This endpoint will return a Product based on it's id
    """
    app.logger.info("Request for product with id: %s", product_id)
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")
    return jsonify(product.serialize()), status.HTTP_200_OK

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_products(product_id):
    """
    Update a Product
    This endpoint will update a Product based the body that is posted
    """
    app.logger.info("Request to update product with id: %s", product_id)
    check_content_type("application/json")
    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")
    product.deserialize(request.get_json())
    product.id = product_id
    product.update()
    return jsonify(product.serialize()), status.HTTP_200_OK

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_products(product_id):
    """
    Delete a Product
    This endpoint will delete a Product based the id specified in the path
    """
    app.logger.info("Request to delete product with id: %s", product_id)
    product = Product.find(product_id)
    if product:
        product.delete()
    return "", status.HTTP_204_NO_CONTENT

@app.route("/products", methods=["GET"])
def list_products():
    """Returns all of the Products"""
    app.logger.info("Request for product list")
    products = []
    category = request.args.get("category")
    name = request.args.get("name")
    available = request.args.get("available")

    if category:
        products = Product.find_by_category(category)
    elif name:
        products = Product.find_by_name(name)
    elif available:
        available_value = available.lower() in ["true", "yes", "1"]
        products = Product.find_by_availability(available_value)
    else:
        products = Product.all()

    results = [product.serialize() for product in products]
    app.logger.info("Returning %d products", len(results))
    return jsonify(results), status.HTTP_200_OK
