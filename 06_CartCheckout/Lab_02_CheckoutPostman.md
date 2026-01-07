# Lab - Create a Cart and Checkout Flow in Postman

### Prerequisites

* A BigCommerce [sandbox store](https://developer.bigcommerce.com/docs/start/about/sandboxes) or [trial store](https://www.bigcommerce.com/essentials/), or a full production store
* [Postman](https://www.postman.com/)
* An existing Postman environment and collection as configured in previous labs

### Shipping Configuration

Your store must be configured with a shipping zone that:

* Includes Austin, TX (or you can feel free to change the details of the shipping address we use)
* Has at least one available shipping method

For more about configuring shipping, see the article below:

**[Shipping Setup](https://support.bigcommerce.com/s/article/Shipping-Setup)**

### Product Prerequisites

Your store should contain at least one product that:

* Is physical
* Is in stock and purchasable
* Has at least one in-stock variant option
* Has no required modifier options
* Qualifies for the available shipping method

## Collection Variables

Make sure the following Postman collection variables are pre-populated (manually or by requests in previous exercises) to support the automated requests.

* `product_id`
* `variant_id`

## Sequence Overview

The workflow we'll be building is an example of the requests potentially involved for a headless storefront to manage carts, checkouts, and payments. The steps involved include retrieving information about a product, adding it to the cart, and completing the billing, shipping and payment steps of checkout. Most of the requests we'll be building use the GraphQL Storefront API, though certain steps like generating a GraphQL token and performing payment processing will require REST API actions.

At a high level, our Postman collection will follow this sequence:

1. **Create** a cart and **add** the product found previously, **storing** the cart and line item IDs.
2. **Get** checkout redirect URLs for the new cart, which would be used if your storefront will direct the customer to BigCommerce native checkout.
3. **Add** a shipping consignment to the checkout with a hard-coded shipping address, then **store** the first available shipping option form the response.
4. **Update** the shipping consignment to **select** the shipping method.
5. **Add** a billing address to the checkout with hard-coded details.
6. **"Complete"** the checkout, resulting in a new order record that will be considered incomplete until payment is applied.

## Exercises

Try the following requests in the "Cart/Checkout" or "Cart/Checkout (Automated)" folder.

### GQL Create Cart

* **Enter** a valid value for `productId` and `variantId` in the GraphQL variables pane of the Body tab.
* **Verify** that all tests succeed.
* **Observe** the cart response data.
* **Record** the cart ID and line item ID for future requests.

**AUTOMATION:** The automated version of the request should have `productId` and `variantId` automatically populated and should save `cart_id` and `line_item_id` collection variables.

### GQL Get Cart

* **Enter** the `cartId` value in the GraphQL variables pane of the Body tab.
* **Observe** the cart response data.

**AUTOMATION:** The automated version of the request should have `cartId` automatically populated.

### GQL Get Cart Redirect URLs

* **Enter** the `cartId` value in the GraphQL variables pane of the Body tab.
* **Verify** that all tests succeed.
* **Observe** the cart response data.
* **Browse** to the `redirectedCheckoutUrl` to see the checkout in action.

**AUTOMATION:** The automated version of the request should have `cartId` automatically populated.

### GQL Get Checkout

* **Enter** the `cartId` value in the GraphQL variables pane of the Body tab.
* **Observe** the checkout response data.

**AUTOMATION:** The automated version of the request should have `cartId` automatically populated.

### GQL Create Consignment

* **Enter** the `cartId` value and a valid `lineItemId` (from "GQL Create Cart") in the GraphQL variables pane of the Body tab.
* **Verify** that all tests succeed.
* **Observe** the checkout response data.
* **Record** the consignment ID and the ID of a valid shipping option from the response.
* **Re-run** "GQL Get Checkout" to see the modified checkout data.

**AUTOMATION:** The automated version of the request should have `cartId` and `lineItemId` automatically populated.

### GQL Select Shipping

* **Enter** the `cartId` and a valid `consignmentId` and `shippingOptionId` (from "GQL Create Consignment") in the GraphQL variables pane of the Body tab.
* **Verify** that all tests succeed.
* **Observe** the checkout response data.
* **Re-run** "GQL Get Checkout" to see the modified checkout data.

**AUTOMATION:** The automated version of the request should have `cartId`, `consignmentId`, and `shippingOptionId` automatically populated.

### GQL Create Billing Address

* **Enter** the `cartId` in the GraphQL variables pane of the Body tab.
* **Update** the address details in the Body as desired.
* **Verify** that all tests succeed.
* **Observe** the checkout response data.
* **Re-run** "GQL Get Checkout" to see the modified checkout data.

**AUTOMATION:** The automated version of the request should have `cartId` automatically populated.

### GQL Complete Checkout

* **Enter** the `cartId` in the GraphQL variables pane of the Body tab.
* **Verify** that all tests succeed.
* **Observe** the order response data.
* **Record** the `orderEntityId` from the response if you intend to complete the subsequent Payments exercise.

**AUTOMATION:** The automated version of the request should have `cartId` automatically populated. It should also save the `order_id` collection variable for subsequent exercises.
