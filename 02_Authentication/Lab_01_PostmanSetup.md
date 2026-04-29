# Lab - Authentication and Postman Setup

## Prerequisites

* A BigCommerce [sandbox store](https://docs.bigcommerce.com/developer/docs/overview/sandboxes) or [trial store](https://www.bigcommerce.com/essentials/), or a full production store
* [Postman](https://www.postman.com/) or a similar API client


## In this lab, you will:

* Generate a store-level v2/v3 API token
* Create a **Storefront Token** (with CORS) for browser/client use → stored in `storefront_token`
* Create a **Private Token** for server-to-server use → stored in `private_storefront_token`
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

## Step 4: Create a Storefront Token for Client Use

You'll create a **Storefront Token** with `allowed_cors_origins` so it can be used from a browser (e.g. for the "View Example" step later). This token is automatically stored in `storefront_token` by the request's test script.

In the "Setup" folder, run the request **"REST Create Storefront Token (client)"**.

* **Verify** that all tests succeed.
* **Verify** that the `storefront_token` variable is now populated in your environment.

## Step 5: View Example With Your Store's Data

The token you created in the previous step will work in a client-side context when the request originates from `bigcommerce.github.io`.

1. **Copy** the `storefront_token` value from your Postman environment.
2. **Go** to [https://bigcommerce.github.io/storefront-api-examples/html-bootstrap-vanillajs/](https://bigcommerce.github.io/storefront-api-examples/html-bootstrap-vanillajs/).
3. **Paste** your store's URL in the "Store URL" field.
4. **Paste** your token into the "Storefront API Token" field.
5. **Click** Submit.
6. **View** the web page.

## Step 6: Create a Private Token for Server-to-Server

For server-to-server GraphQL requests (and the rest of this course), you'll use a **Private Token**. Unlike the Storefront Token, a Private Token uses a different endpoint (`/api-token-private`) and requires `scopes` in the request body. This token is automatically stored in `private_storefront_token` and is used by the collection's Bearer Token authorization for all GraphQL requests.

In the "Setup" folder, run the request **"REST Create Private Token (server)"**.

* **Verify** that all tests succeed.
* **Observe** the token in the response.
* **Verify** that the `private_storefront_token` variable is now populated in your environment.

After your token is successfully created, try the "GQL Get Category Tree" request in the "Catalog" folder.
