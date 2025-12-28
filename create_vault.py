import boto3
import base64
import json

# Initialize KMS client
kms_client = boto3.client('kms', region_name='us-east-1')

# Example: vault ID for a customer
vault_id = "customer_123"

# Generate encrypted data key
response = kms_client.generate_data_key_without_plaintext(
    KeyId="arn:aws:kms:region:account-id:key/key-id",
    KeySpec="AES_256"
)

# Encrypted data key
encrypted_data_key = base64.b64encode(response['CiphertextBlob']).decode('utf-8')

# Simulate storing the encrypted key in a vault (JSON file)
vault_file = f"{vault_id}_vault.json"
with open(vault_file, 'w') as f:
    json.dump({"encrypted_data_key": encrypted_data_key}, f)

print(f"Vault created for {vault_id}, encrypted data key stored in {vault_file}")
