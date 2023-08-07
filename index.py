import os

from dotenv import load_dotenv
load_dotenv()

from auth.auth import Auth
from folder.folder import Folder

# Authentication
auth = Auth(
    os.environ['TEST_CLIENT_ID'], 
    os.environ['TEST_CLIENT_SECRET'], 
    os.environ['TEST_MID'], 
    os.environ['TEST_AUTH_URI']
)

auth.get_access_token()

folder = Folder()
res = folder.create('TESTING TESTING', os.environ['TEST_SOAP_URI'], auth.access_token)
print(res.content)