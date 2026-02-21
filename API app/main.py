import api_proxy.api_methods as methods
import requests as req
import pprint
import time


API_key = '4642a9e1ddea44f8a003a5ae0e1f1ebf'

if __name__ == '__main__':
    result = methods.get_top_headlines(q='apple', api_key=API_key)
    pprint.pprint(result)
    time.sleep(3)

    result = methods.get_everything(q='apple', api_key=API_key)
    pprint.pprint(result)
    time.sleep(3)

    result = methods.get_sources(api_key=API_key)
    pprint.pprint(result)
