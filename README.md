# service-url-shortener

## Deploy

> Install `make` or refer to Makefile

### Environment variables

```
DB_USER=user
DB_PASS=password
DB_HOST=database
DB_PORT=5432
DB_NAME=url_shortener
JWT_SECRET=secret
```

### Docker

- `make docker-compose-up`

### Local

1. prepare a postgresql instance
2. modify environment variables
3. `make serve` or `make dev` for development environment

## Tests

- `make test`

## DB migration

- `make init`

## OpenAPI

- http://localhost:8000/docs
- http://localhost:8000/redocs
