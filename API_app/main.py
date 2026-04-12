from api_proxy import *
from analytics.article_anal import anal
import pprint
import json
import time

API_key = '4642a9e1ddea44f8a003a5ae0e1f1ebf'

if __name__ == '__main__':
    articles_from_yesterday(api_key=API_key)