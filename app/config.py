from os import environ as env

db: dict = {"url": env.get("DB_URL", "mongodb://mongodb:27017")}
jwt: dict = {"key": env.get("JWT_KEY", "secret")}
