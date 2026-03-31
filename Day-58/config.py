import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret")
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DATABASE = "test"
    MYSQL_PORT = 3306