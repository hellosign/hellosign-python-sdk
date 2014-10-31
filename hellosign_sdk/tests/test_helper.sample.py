import logging
import os

# NOTE: Setup instructions
# Before running the tests, do the following
# ===========================================
# 1. Create an account, upgrade to Business and add an API plan
# 2. Create an api app, set the client id and secret as environment variables
# 3. Create two templates, both with a single role named 'Signer'

# Logging
logging.basicConfig(level=logging.INFO)

# Credentials
api_key = os.environ.get('HELLOSIGN_API_KEY')

client_id = os.environ.get('HELLOSIGN_API_CLIENT_ID')
client_secret = os.environ.get('HELLOSIGN_API_CLIENT_SECRET')
