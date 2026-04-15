# Changelog: GraphQL Storefront API Labs

**Date:** 2026-04-15
**Comparison:** Changes from main branch
**Collection file:** `GraphQL Storefront API Labs.postman_collection.json`

## Global Changes

### Collection Auth

The bearer token variable was updated from `{{storefront_token}}` to `{{private_storefront_token}}`.

## Setup

### Added Requests

- `REST Create Private Token (server)`

### Removed Requests

- `REST Create Storefront Token (server to server)`
- `REST Create Storefront CIT`

### Modified Requests

#### `REST Create Storefront Token (with origin)` → `REST Create Storefront Token (client)`

- **Name changed**
- **Test scripts updated**
