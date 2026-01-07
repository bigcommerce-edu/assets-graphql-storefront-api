# Optional Lab - Complete Checkout Flow with Payment

### Prerequisites

* A BigCommerce [sandbox store](https://developer.bigcommerce.com/docs/start/about/sandboxes) or [trial store](https://www.bigcommerce.com/essentials/), or a full production store
* [Postman](https://www.postman.com/)
* An existing Postman environment and collection as configured in previous labs

### Payment Configuration

Your store must have the following payment configuration:

* A payment gateway must be enabled and configured in sandbox/test mode.The &quot;Enable test credit card payments&quot; option in payment settings is _not_ sufficient.

A gateway in sandbox mode is important for the successful use of a dummy credit card number, and the enabled payment method must be compatible with the Payments API. The following shows an example of enabling Test Mode with the Stripe payment gateway:

![Image](https://storage.googleapis.com/bigcommerce-production-dev-center/learning-edu/graphql-storefront-api/stripe-test-mode.png)

Consider setting up a sandbox account for one of the following payment gateways:

* [Stripe](https://dashboard.stripe.com/register)
* [Authorize.net](https://developer.authorize.net/hello_world/sandbox.html)
* [Cybersource](https://developer.cybersource.com/hello-world/sandbox.html)

For more about configuring payments, see the article below:

* [Online Payment Methods](https://support.bigcommerce.com/s/article/Online-Payment-Methods)

**An Important Note About Payments**

Our example requests will involve directly supplying a credit card number. For real-world implementations directly handling credit card numbers, you must consider the implications for [PCI DSS](https://www.pcisecuritystandards.org/) compliance. If an application passes credit card information to BigCommerce, that application's PCI compliance and Cardholder Data Environment (CDE) are not managed by BigCommerce.

You can minimize your PCI compliance burden by using the [Stored Credit Cards feature](https://support.bigcommerce.com/s/article/Enabling-Stored-Payment-Methods) provided by BigCommerce. Assuming a cart has a customer ID associated with it, and the customer has previously stored a credit card with BigCommerce, the application can [use the customer's stored payment method to make a payment](https://developer.bigcommerce.com/docs/store-operations/payments#stored-cards-and-paypal-accounts) instead of directly entering a credit card number.

Redirecting to or embedding the BigCommerce checkout means sensitive payment data is never directly entered or transmitted by your frontend application, leaving the burden of PCI compliance to BigCommerce. This is an advantage of this approach. Carefully consider PCI compliance when planning your headless implementation.

## Collection Variables

Make sure the following Postman collection variables are pre-populated (manually or by requests in previous exercises) to support the automated requests.

* `order_id`

## Exercises

Try the following requests from the "Cart/Checkout" or "Cart/Checkout (Automated)" folder.

### REST Get Payment Methods

* **Enter** a valid `order_id` query param.
* **Observe** the payment method response data.
* **Record** a payment method ID.

**AUTOMATION:** The automated version of the request should have `order_id` automatically populated and should save the `payment_method_id` collection variable.

### REST Create Pay Token

* **Enter** a valid `order_id` in the Body tab.
* **Verify** that all tests succeed.
* **Observe** the response data.
* **Record** the token ID from the response.

**AUTOMATION:** The automated version of the request should have `order_id` automatically populated and should save the `pat` collection variable.

### REST Process Payment

* **Enter** a valid `payment_method_id` in the Body tab.
* **Enter** the PAT value from the previous request in the Authorization header, in the form "PAT <value>".
* **Verify** that all tests succeed.
* **Observe** the payment status response data.

**AUTOMATION:** The automated version of the request should have `payment_method_id` and the Authorization header automatically populated.
