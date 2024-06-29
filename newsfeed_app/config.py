import os

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', '12345')
DB_NAME = os.getenv('DB_NAME', 'newsfeed_app')
