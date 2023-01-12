from dotenv import load_dotenv
import os

load_dotenv()


DB_USER = os.getenv('db_user')
DB_PASSWORD = os.getenv('db_password')
DB_HOST = os.getenv('db_host')
DB_PORT = os.getenv('db_port')
DB_NAME = os.getenv('db_name')
DB_DRIVER = os.getenv('db_driver', 'psycopg2')


SECRET_JWT = os.getenv('secret_jwt')
ALGORITHM_JWT = os.getenv('algorithm_jwt', 'HS256')
TOKEN_LIFETIME_MINUTES = int(os.getenv('token_lifetime_minutes', '30'))