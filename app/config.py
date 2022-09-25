from pydantic import BaseSettings


class DB(BaseSettings):
    user: str = "user"
    passwd: str = "password"
    host: str = "localhost"
    port: str = "5432"
    name: str = "url_shortener"

    class Config:
        env_prefix = "db_"

    @property
    def url(self) -> str:
        return f"postgresql+pg8000://{self.user}:{self.passwd}@{self.host}:{self.port}/{self.name}"


class JWT(BaseSettings):
    secret: str = "secret"

    class Config:
        env_prefix = "jwt_"


db = DB()
jwt = JWT()
