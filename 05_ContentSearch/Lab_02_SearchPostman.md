# Lab - Create a Search and Filter Flow in Postman

### Prerequisites

* A BigCommerce [sandbox store](https://developer.bigcommerce.com/docs/start/about/sandboxes) or [trial store](https://www.bigcommerce.com/essentials/), or a full production store
* [Postman](https://www.postman.com/)
* An existing Postman environment and collection as configured in previous labs

### Catalog Data Prerequisites

In the requests you'll be creating, you'll be starting out querying for products on a specific search term, then capturing and applying other available filters to continue narrowing the results set. We'll be filtering on these facets:

* A top-level category
* A variant option value


In order to support this flow, you'll need a pool of at least four products following these guidelines:

* All products must include the same search term in their name.
* Various products should be assigned to the same top-level categories.
* All products must include a variant option with the same name.
* Various values for the variant option should be shared among different products, but not all products.


The common category assignments and values between products should allow for varied results sets depending on what filters are applied. Below is an example product set.


| Product Name | Categories | Variant Option |
| --- | --- | --- |
| Athletic T-Shirt | Fitness, Casual Wear, Professional Wear | Color: Black, Grey, Red |
| Casual T-Shirt | Casual Wear, On Sale | Color: White, Red |
| Professional T-Shirt | Fitness, Professional Wear, On Sale | Color: Black, White, Blue |
| Striped T-Shirt | Casual Wear, Professional Wear, On Sale | Color: Grey, Blue, Black |

The following requests in the "Search/Filter" or "Search/Filter (Automated)" folder will create the categories and products shown above:

* REST Create Example Categories
* REST Create Example Product 1
* REST Create Example Product 2
* REST Create Example Product 3
* REST Create Example Product 4

It will be necessary to assign the products to their categories after running these requests.

In your Product Filters settings in the BigCommerce control panel, make sure the **Category** and **Variant** options are enabled as visible filters at the global or channel level.

## Collection Variables

Make sure the following Postman collection variables are pre-populated to support the automated requests.

* `filter_search_term`: The search term used to filter product results

## Exercises

Try the following requests in the "Search/Filter" or "Search/Filter (Automated)" folder.

### GQL Product Search

This requests searches on a specific term without filtering the product results further.

* **Enter** a value for `searchTerm` in the GraphQL variables pane of the Body tab.
* **Observe** the product response data.
* **Record** a valid category ID from the `filters` in the response.

**AUTOMATION:** The automated version of the request should have `searchTerm` automatically populated as long as the `filter_search_term` collection variable is set. The request should also save a `filter_category` collection variable with the first available category ID.

### GQL Product Search - Cat

This request further refines the search by adding a category filter.

* **Enter** both a `searchTerm` and `categoryId` in the GraphQL variables pane of the Body tab.
* **Observe** the product response data.
* **Record** a valid attribute name and value from the `filters` in the response.

**AUTOMATION:** The automated version of the request should have `searchTerm` and `categoryId` automatically populated. The request should also save `filter_variant_attr_name` and `filter_variant_attr_val` collection variables with the first available product attribute filter.

### GQL Product Search - Cat, Variant

This request further refines the search by adding a product attribute filter.

* **Enter** a `searchTerm`, `categoryId`, `variantAttrName`, and `variantAttrVal` in the GraphQL variables pane of the Body tab.
* **Observe** the product response data.

**AUTOMATION:** The automated version of the request should have all required GraphQL variables automatically populated from the previous requests.
