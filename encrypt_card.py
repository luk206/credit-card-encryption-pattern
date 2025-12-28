import boto3
import json
import base64

kms_client = boto3.client('kms', region_name='us-east-1')

vault_file = "customer_123_vault.json"
with open(vault_file, 'r') as f:
    vault = json.load(f)

encrypted_data_key = base64.b64decode(vault['encrypted_data_key'])

# Decrypt data key in memory
response = kms_client.decrypt(
    CiphertextBlob=encrypted_data_key
)
data_key = response['Plaintext']

# Example: encrypt credit card
credit_card_plain = b"4111111111111111"
from cryptography.fernet import Fernet
fernet = Fernet(base64.urlsafe_b64encode(data_key[:32]))  # Fernet needs 32 bytes key
encrypted_card = fernet.encrypt(credit_card_plain)

# Store encrypted card
vault['encrypted_card'] = base64.b64encode(encrypted_card).decode('utf-8')
with open(vault_file, 'w') as f:
    json.dump(vault, f)

print("Credit card encrypted and stored in vault")
