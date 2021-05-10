import os

"""
Check what env variables are set
"""

if __name__ == '__main__':
    print("AZ ten ID is: {id}".format(id=os.environ['AZURE_TENAT_ID']))
    print("AZ client ID is: {id}".format(id=os.environ['AZURE_CLIENT_ID']))
    print("AZ client secret is: {id}".format(id=os.environ['AZURE_CLIENT_SECRET']))
