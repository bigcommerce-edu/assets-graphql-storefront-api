Request name:
GQL Get Checkout

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

| Header       | Value            |
|--------------|------------------|
| Accept       | application/json |
| Content-Type | application/json |


Body:
```
query GetCart(
  $cartId: String!
) {
    site {
        checkout(entityId: $cartId) {
            cart {
                id
                entityId
                currencyCode
                baseAmount {
                    value
                }
                amount {
                    value
                }
            }
            shippingCostTotal {
                value
            }
            handlingCostTotal {
                value
            }
            taxTotal {
                value
            }
            subtotal {
                value
            }
            grandTotal {
                value
            }
            billingAddress {
                firstName
                lastName
                email
                address1
                city
                stateOrProvince
                countryCode
                postalCode
                phone
            }
            shippingConsignments {
                address {
                    firstName
                    lastName
                    email
                    address1
                    city
                    stateOrProvince
                    countryCode
                    postalCode
                    phone
                }
                availableShippingOptions {
                    description
                    type
                }
                selectedShippingOption {
                    description
                    type
                }
                shippingCost {
                    value
                }
                handlingCost {
                    value
                }
                lineItemIds
            }
        }
    }
}
```

Variables:
```
{
    "cartId": "{{cart_id}}"
}
```