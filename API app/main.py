from api_proxy import get_top_headlines, get_everything, get_sources
import pprint
import time



API_key = '4642a9e1ddea44f8a003a5ae0e1f1ebf'

if __name__ == '__main__':
    result = get_top_headlines(q='apple', api_key=API_key)
    pprint.pprint(result)
    time.sleep(3)

    result = get_everything(q='apple', api_key=API_key)
    pprint.pprint(result)
    time.sleep(3)

    result = get_sources(api_key=API_key)
    pprint.pprint(result)

