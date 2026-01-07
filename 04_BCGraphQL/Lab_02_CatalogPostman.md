# Lab - Create a Catalog Flow in Postman

### Prerequisites

* A BigCommerce [sandbox store](https://developer.bigcommerce.com/docs/start/about/sandboxes) or [trial store](https://www.bigcommerce.com/essentials/), or a full production store
* [Postman](https://www.postman.com/)
* An existing Postman environment and collection as configured in previous labs
* At least one visible top-level category with at least one visible child category
* At least 6 products

### Category prerequisites

Your BigCommerce store must contain a top-level category (which can be different than the category with child categories) that:

* Is visible
* Has products assigned

### Product prerequisites

Your BigCommerce store must contain at least one product that:

* Is physical
* Is in stock and purchasable
* Has at least one in-stock variant option
* Has no required modifier options

## Exercises

Try the following requests in the "Catalog" or "Catalog (Automated)" folder.

### GQL Get Category Tree

* **Observe** the category response data.

**AUTOMATION:** The automated version of the request should save a `category_id` collection variable with the ID of the first category with products.

### GQL Get Category

* **Enter** a value for `categoryId` in the GraphQL variables pane of the Body tab.
* **Observe** the category response data.

**AUTOMATION:** The automated version of the request should have `categoryId` automatically populated by the collection variable from "Get Category Tree".

### GQL Get Paginated Products

* **Enter** an empty value for `lastProductCursor` in the GraphQL variables pane of the Body tab.
* **Observe** the product response data.
* **Record** `site.products.pageInfo.endCursor` from the response and **enter** it as the `lastProductCursor` variable value.
* **Re-run** the request to see the next page of results.

**AUTOMATION:** The automated version of the request is designed to page through results successively with each request. This is done with the `last_product_cursor` collection variable, so **reset** this variable to start again with the first page. The automated request should also save the `product_id` and `variant_id` collection variables with the IDs of the first physical product found with available inventory. This will be used with future automated requests.

### GQL Get Product

* **Enter** a valid product ID for `productId` in the GraphQL variables pane of the Body tab.
* **Observe** the product response data.

**AUTOMATION:** The automated version of the request should have `productId` automatically populated.
