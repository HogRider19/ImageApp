from dotenv import load_dotenv
import os


env_file_path = os.getenv('env_file_path', None)

load_dotenv(dotenv_path=env_file_path)

DB_USER = os.getenv('db_user', 'postgres')
DB_PASSWORD = os.getenv('db_password', 'postgres')
DB_HOST = os.getenv('db_host')
DB_PORT = os.getenv('db_port', '')
DB_NAME = os.getenv('db_name', 'postgres')
DB_DRIVER = os.getenv('db_driver', 'psycopg2')

TESTING_DB_NAME = os.getenv('testing_db_name', 'testing_db')

SECRET_JWT = os.getenv('secret_jwt')
ALGORITHM_JWT = os.getenv('algorithm_jwt', 'HS256')
TOKEN_LIFETIME_MINUTES = int(os.getenv('token_lifetime_minutes', '30'))

MEDIA_BASE_DIR = 'media/'

DB_PORT = f":{DB_PORT}" if DB_PORT and DB_PORT[0] != ':' else DB_PORT

LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': { 
        'stremm_handler': { 
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file_handler': { 
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'logs/logs.log',
            'mode': 'a',
            'encoding': 'utf8',
        },
    },
    'loggers': { 
        '': { 
            'handlers': ['file_handler'],
            'level': 'WARNING',
            'propagate': False
        },
    } 
}