from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

"""
Function used to check if Azure set-up is working correctly
"""

#Initialize your creds
def_cred = DefaultAzureCredential()

#Create secret client
secret_client = SecretClient(
    vault_url="https://stuff21.vault.azure.net/",
    credential=def_cred
)

#Get secret
my_secret = secret_client.get_secret(
    name="fishy-data-conn-string"
)

#Print secret if you have acess
print(my_secret.value)