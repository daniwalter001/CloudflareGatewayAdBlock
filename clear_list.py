from typing import List
import requests
import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger("cloudflare")
load_dotenv()


CF_API_TOKEN = os.getenv("CF_API_TOKEN")
CF_IDENTIFIER = os.getenv("CF_IDENTIFIER")

print(CF_IDENTIFIER)
print(CF_API_TOKEN)

if not CF_API_TOKEN or not CF_IDENTIFIER:
    raise Exception("Missing Cloudflare credentials")

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {CF_API_TOKEN}"})

def clear_cloudflare_policies(prefix:str):
    pass
