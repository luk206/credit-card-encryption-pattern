import boto3
import json
import base64
from cryptography.fernet import Fernet

kms_client = boto3.client('kms', region_name='us-east-1')

vault_file = "customer_123_vault.json"
with open(vault_file, 'r') as f:
    vault = json.load(f)

encrypted_data_key = base64.b64decode(vault['encrypted_data_key'])
encrypted_card = base64.b64decode(vault['encrypted_card'])

# Decrypt data key in memory
response = kms_client.decrypt(CiphertextBlob=encrypted_data_key)
data_key = response['Plaintext']

# Decrypt credit card
fernet = Fernet(base64.urlsafe_b64encode(data_key[:32]))
credit_card_plain = fernet.decrypt(encrypted_card)

print(f"Decrypted credit card: {credit_card_plain.decode('utf-8')}")
