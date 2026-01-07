# Lab - Create a Customer Flow in Postman

### Prerequisites

* A BigCommerce [sandbox store](https://developer.bigcommerce.com/docs/start/about/sandboxes) or [trial store](https://www.bigcommerce.com/essentials/), or a full production store
* [Postman](https://www.postman.com/)
* An existing Postman environment and collection as configured in previous labs

### Form Fields Configuration

To get the full benefit from this workflow, you should make sure that you have configured one to three custom Form Fields for customer account signup.

In your BigCommerce control panel, manage Form Fields in Settings > Advanced > Account sign up form. You'll be building support for Account Signup Fields, not Address Fields. The following field types will be supported in your Postman logic, so make sure to set up one to three custom fields of one or more of these types.

* Pick List
* Radio Buttons
* Date Field
* Text Field

## Collection Variables

Make sure the following Postman collection variables are pre-populated (manually or by requests in previous exercises) to support the automated requests.

* `customer_email`: The email of a new customer that will be registered
* `customer_password`: The password that will be set for the newly registered customer

## Exercises

Try the following requests in the "Customer" or "Customer (Automated)" folder.

### GQL Get Form Fields

This request will retrieve information on any custom registration fields configured in your store.

* **Observe** the form field response data.
* **Record** field IDs and value IDs for any required fields.
* **Note** `minDate` and `maxDate` values for any required date fields.

**AUTOMATION:** The automated version of the request should automatically save `customer_multiple_choice`, `customer_dates`, and `customer_texts` collection variables for any existing custom fields that are a multiple choice, date, or text type. The values saved for these variables will be in array format, matching the GraphQL schema expected by the `registerCustomer` mutation.

* For multiple choice fields, the first available value will be saved.
* For date fields, the minimum date, default date, or maximum date will be saved.
* For text fields, the value "Test Value" will be saved.

### GQL Register Customer

* **Enter** an `email` and `password` value for the customer to be registered, in the GraphQL variables pane of the Body tab.
* **Enter** values, as appropraite, for the `multipleChoices`, `dates`, and `texts` variables.
* **Verify** that all tests succeed.
* **Observe** the customer response data.

**AUTOMATION:** The automated version of the request should have `email` and `password` automatically populated. Any values for custom fields captured in the previous request should also automatically populate `multipleChoices`, `dates`, and `texts`.

### GQL Customer Login

* **Enter** an existing customer's `email` and `password` in the GraphQL variables pane of the Body tab.
* **Verify** that all tests succeed.
* **Observe** the customer response data.
* **Record** the customer ID and the customer access token from the response.

**AUTOMATION:** The automated version of the request should have `email` and `password` automatically populated and should save `customer_id` and `customer_access_token` collection variables from the response.

### GQL Get Customer

This request simulates a logged-in customer with the customer access token header.

* **Enter** the previously received customer access token as the value of `X-Bc-Customer-Access-Token` in the Headers tab.
* **Observe** the customer response data.

**AUTOMATION:** The automated version of the request should have the `X-Bc-Customer-Access-Token` header automatically populated with the token from your login request.

### GQL Add Customer Address

This request simulates a logged-in customer with the customer access token header.

* **Enter** the previously received customer access token as the value of `X-Bc-Customer-Access-Token` in the Headers tab.
* **Update** address values as desired in the GraphQL variables pane of the Body tab.
* **Verify** that all tests succeed.
* **Observe** the customer address response data.

**AUTOMATION:** The automated version of the request should have the `X-Bc-Customer-Access-Token` header automatically populated with the token from your login request. 

### OPTIONAL: Additional Logged-in Requests

If you have custom pricing set up in your store for specific customer groups, try the following with the "Automated" version of your Customer requests:

* Assign a registered customer to a customer group with custom pricing.
* Set the appropriate details on the `customer_email` and `customer_password` collection variables.
* Run the "GQL Customer Login" request to capture a customer access token for the customer.
* Re-run the "GQL Get Product" request in the "Catalog" folder after setting the `X-Bc-Customer-Access-Token` header with the value `{{customer_access_token}}`.

Product data in the responses should reflect the customer group pricing.

### OPTIONAL: GQL Request Password Reset

* **Enter** a valid `email` in the GraphQL variables pane of the Body tab. (This email _must_ be a real address to which you have access!)
* **Verify** that all tests succeed.
* **Observe** the response data.
* **Open** the password reset email that was received.

Look for the reset link in the email, which should have a URL in the format `https://{store-domain}/my-password-reset?c={customer-ID}&t=**{token}**`. Record the token value (the `t` querystring param) for the next request.

**AUTOMATION:** The automated version of the request should have `customer_email` automatically populated.

### OPTIONAL: GQL Reset Password

* **Enter** the appropriate `customerId` and a new `password` in the GraphQL variables pane of the Body tab.
* **Enter** the token obtained from the reset email as the value of the `token` GraphQL variable.
* **Verify** that all tests succeed.
* **Observe** the response data.

**AUTOMATION:** Prior to running the request, manually change the `customer_password` collection variable to the desired new password, verify that the `customer_id` collection variable matches the customer email the password reset was initiated for, and set the token obtained from the reset email in the `password_reset_token` collection variable. The automated version of the request should then have `customerId`, `token` and `password` automatically populated.
