    def test_get_product(self):
        """It should Get a single Product"""
        # get the id of a product
        test_product = self._create_products(1)[0]
        response = self.client.get(f"{BASE_URL}/{test_product.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(data["name"], test_product.name)

    def test_update_product(self):
        """It should Update an existing Product"""
        # create a product to update
        test_product = ProductFactory()
        response = self.client.post(BASE_URL, json=test_product.serialize())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # update the product
        new_product = response.get_json()
        new_product["description"] = "unknown"
        response = self.client.put(f"{BASE_URL}/{new_product['id']}", json=new_product)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_product = response.get_json()
        self.assertEqual(updated_product["description"], "unknown")

    def test_delete_product(self):
        """It should Delete a Product"""
        test_product = self._create_products(1)[0]
        response = self.client.delete(f"{BASE_URL}/{test_product.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(response.data), 0)
        # make sure they are deleted
        response = self.client.get(f"{BASE_URL}/{test_product.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_product_list(self):
        """It should Get a list of Products"""
        self._create_products(5)
        response = self.client.get(BASE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(len(data), 5)

    def test_query_product_list_by_name(self):
        """It should Query Products by Name"""
        products = self._create_products(10)
        test_name = products[0].name
        name_products = [product for product in products if product.name == test_name]
        response = self.client.get(BASE_URL, query_string=f"name={quote_plus(test_name)}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(len(data), len(name_products))
        for product in data:
            self.assertEqual(product["name"], test_name)

    def test_query_product_list_by_category(self):
        """It should Query Products by Category"""
        products = self._create_products(10)
        test_category = products[0].category
        category_products = [product for product in products if product.category == test_category.name]
        response = self.client.get(BASE_URL, query_string=f"category={test_category.name}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(len(data), len(category_products))
        for product in data:
            self.assertEqual(product["category"], test_category.name)

    def test_query_product_list_by_availability(self):
        """It should Query Products by Availability"""
        products = self._create_products(10)
        test_available = products[0].available
        available_products = [product for product in products if product.available == test_available]
        response = self.client.get(BASE_URL, query_string=f"available={str(test_available).lower()}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.get_json()
        self.assertEqual(len(data), len(available_products))
        for product in data:
            self.assertEqual(product["available"], test_available)
