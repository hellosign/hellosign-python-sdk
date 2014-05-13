import logging
import os

# Logging
logging.basicConfig(level=logging.INFO)

# Credentials
api_key = os.environ.get('HELLOSIGN_API_KEY')

client_id = os.environ.get('HELLOSIGN_API_CLIENT_ID')
client_secret = os.environ.get('HELLOSIGN_API_CLIENT_SECRET')
