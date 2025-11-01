import requests
import os
from dotenv import load_dotenv

load_dotenv()
sams_api = os.getenv('sams_api')

def call_sams(entity_name):
    call = 'https://api.sam.gov/entity-information/v4/exclusions?api_key=' + sams_api
    print(call)