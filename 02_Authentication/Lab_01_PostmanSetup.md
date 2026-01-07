# Lab - Authentication and Postman Setup

## Prerequisites

* A BigCommerce [sandbox store](https://developer.bigcommerce.com/docs/start/about/sandboxes) or [trial store](https://www.bigcommerce.com/essentials/), or a full production store
* [Postman](https://www.postman.com/) or a similar API client


## In this lab, you will:

* Generate a store-level v2/v3 API token
* Create a GraphQL Storefront API token
* View the GraphQL Storefront API example with your own store's data


## Step 1: Create a Store-level API Account

1. **Log in** to your BigCommerce store.
2. **Navigate** to _Settings > Store-level API Accounts._
3. **Click** the Create API Account button.
4. **Choose** &quot;V2/V3 API token&quot; as the token type.
5. **Type** a name for the API Account.
6. **Configure** OAuth scopes as follows (some of these scopes are for later labs).


| Scope | Permission |
|---|---|
| Create payments | create |
| Get payment methods | read-only |
| Storefront API Tokens | manage |
| Storefront API Customer Impersonation Tokens | manage |

7. **Click** the Save button.
8. **Copy** the Access Token and save the API account information in a place you can access later.

## Step 2: Configure a Postman Environment

You'll need an API client to craft the request to create a GraphQL Storefront API token. These instructions will assume the use of Postman.

1. **Record** the store hash for your BigCommerce store. You can find this in the URL of your control panel, which is in the format `https://store-{store hash}.mybigcommerce.com`.
2. In Postman, **create** a new environment and give it a name.
3. **Create** the following environment variables.

| Variable Name | Value |
| --- | --- |
| `v3_token` | The access token of your store-level V2/V3 API account |
| `store_hash` | Your store hash |
| `storefront_channel_id` | 1 |

4. **Select** the environment in the environment drop-down.

## Step 3: Import Collection

Import the [GraphQL Storefront API collection](../GraphQL%20Storefront%20API%20Labs.postman_collection.json).

## Step 4: Create a GraphQL Storefront Token with Allowed Origins

For your first token, you'll specify `allowed_cors_origins`, configuring a token that will be usable client-side from a specific origin domain (bigcommerce.github.io).

In the "Setup" folder, run the request **"REST Create Storefront Token (with origin)"**.

* **Verify** that all tests succeed.
* **Record** the `token` value from the response.

## Step 5: View Example With Your Store's Data

The token you created in the previous step will work in a client-side context when the request originates from `bigcommerce.github.io`.

1. **Go** to [https://bigcommerce.github.io/storefront-api-examples/html-bootstrap-vanillajs/](https://bigcommerce.github.io/storefront-api-examples/html-bootstrap-vanillajs/).
2. **Paste** your store's URL in the "Store URL" field.
3. **Paste** your token into the "Storefront API Token" field.
4. **Click** Submit.
5. **View** the web page.

## Step 6: Create a GraphQL Storefront Token with for Server-to-Server

The next request will be nearly identical to the previous, but without specifying `allowed_cors_origins`. This token will be suitable for using server-to-server.

The automation contained in the following request in the imported collection will store this server-to-server token in your environment for automatic use in the authentcation of all future requests.

In the "Setup" folder, run the request **"REST Create Storefront Token (server to server)"**.

* **Verify** that all tests succeed.
* **Observe** the token in the response.
* **Verify** that the `storefront_token` variable is now populated on your collection.

After your token is successfully created, try the "GQL Get Category Tree" request in the "Catalog" folder.
