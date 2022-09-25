# service-url-shortener

## Deploy

> Install `make` or refer to Makefile

- Environment variables

```
DB_USER=user
DB_PASS=password
DB_HOST=database
DB_PORT=5432
DB_NAME=url_shortener
JWT_SECRET=secret
```
- dependencies
  - [PDM](https://pdm.fming.dev/latest/)
  - `make`

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

## Idea and some improvement

### Database schema design

![db](https://i.imgur.com/cwW50y2.png)

I wanted to use MongoDB at first. I finally decided to use PostgreSQL because I didn't find a suitable migration tool for MongoDB in python.

### API design

I design these API in pure "RESTful" way. I konw it is not necessary. I just want to try to do that.

### Test

These tests for now is only test the API can work correctly. It is not a full unit test and it's still have many things to improve. For example, most of the tests should not depend on database connection. It's better to use `mock`.

### FastAPI

I have no many experience about this framework. I choose to use it because its ability to generate OpenAPI automatically. It really helps development more convenient. But I still think that write OpenAPI first before write code is better if possible.

### Response schema

I think just return data in JSON response is a bad idea. So I keep response has "msg", "err", "data" fields. And all the response should be consistent but I have not found proper way to set all the response. Some response like 500 error will show the default response.

### PDM

Just want to try PEP 582 :)
