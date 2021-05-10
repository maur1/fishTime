import datetime
import logging
import requests
import json
import logging
import azure.functions as func

from typing import List, Dict

from .gather_fish import gather_data

from azure.storage.blob import ContainerClient
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def main(mytimer: func.TimerRequest) -> None:

    # Initialize credentials
    default_creds = DefaultAzureCredential()

    # Connect to key vault and authenticate
    sigma_keyvalut = SecretClient(
        vault_url='https://stuff21.vault.azure.net/',
        credential=default_creds
    )

    # Grab Blob connection string from keyvault 
    blob_connection_string = sigma_keyvalut.get_secret(
        name='fishy-data-conn-string'
    )

    # Connect to container storage - exist inside the storage
    container_client = ContainerClient.from_connection_string(
        conn_str=blob_connection_string.value,
        container_name="fishydata"
    )

    # Get fish data
    fishy_dict = gather_data()


    # Create a dynamic file name
    filename = "fishyData/fishes_{ts}.csv".format(
        ts=datetime.datetime.now().timestamp()
    )

    container_client.upload_blob(
        name=filename,
        data=json.dumps(obj=fishy_dict, indent=4),
        blob_type='BlockBlob'
    )

    logging.info('File loaded to Azure Successfully...')

    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
