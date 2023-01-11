from dotenv import load_dotenv
import os

load_dotenv()


DB_USER = os.getenv('db_user')
DB_PASSWORD = os.getenv('db_password')
DB_HOST = os.getenv('db_host')
DB_PORT = os.getenv('db_port')
DB_NAME = os.getenv('db_name')
DB_DRIVER = os.getenv('db_driver')