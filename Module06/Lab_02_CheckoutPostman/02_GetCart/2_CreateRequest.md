Request name:
GQL Get Cart

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
        cart(entityId: $cartId) {
            id
            entityId
            currencyCode
            baseAmount {
                value
            }
            amount {
                value
            }
            lineItems {
                physicalItems {
                    entityId
                    productEntityId
                    variantEntityId
                    sku
                    name
                    imageUrl
                    quantity
                    listPrice {
                        value
                    }
                    originalPrice {
                        value
                    }
                    salePrice {
                        value
                    }
                }
                digitalItems {
                    entityId
                    productEntityId
                    variantEntityId
                    sku
                    name
                    imageUrl
                    quantity
                    listPrice {
                        value
                    }
                    originalPrice {
                        value
                    }
                    salePrice {
                        value
                    }
                }
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