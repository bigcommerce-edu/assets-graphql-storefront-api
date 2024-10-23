Request name:
GQL Get Customer

Disable cookie jar:
On

Authorization:
Inherit auth from parent

Request method:
POST

URL:
```
https://store-{{store_hash}}-{{storefront_channel_id}}.mybigcommerce.com/graphql
```

Headers:

| Header                     | Value                     |
|----------------------------|---------------------------|
| Accept                     | application/json          |
| Content-Type               | application/json          |
| X-Bc-Customer-Access-Token | {{customer_access_token}} |

Body:
```
query GetCustomer {
    customer {
        entityId
        customerGroupId
        email
        firstName
        lastName
        addresses {
            edges {
                node {
                    firstName
                    lastName
                    address1
                    city
                    countryCode
                    stateOrProvince
                    phone
                    postalCode
                }
            }
        }
    }
}
```
