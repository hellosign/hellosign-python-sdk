import logging
import os

logging.basicConfig(level=logging.INFO)

# Logging
logging.basicConfig(level=logging.INFO)

# Credentials
api_key = os.environ.get('HELLOSIGN_API_KEY')

client_id = os.environ.get('HELLOSIGN_API_CLIENT_ID')
secret = os.environ.get('HELLOSIGN_API_CLIENT_SECRET')
