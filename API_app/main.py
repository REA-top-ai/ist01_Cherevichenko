from api_proxy import get_top_headlines, get_everything, get_sources
from analytics.article_anal import anal
import pprint
import json
import time

API_key = '4642a9e1ddea44f8a003a5ae0e1f1ebf'

if __name__ == '__main__':
    result = get_top_headlines(q='apple', api_key=API_key)
    pprint.pprint(result)
    time.sleep(3)

    result = get_everything(q='apple', api_key=API_key)
    anal_result = anal(result)
    print(json.dumps(anal_result, ensure_ascii=False, indent=4))
    time.sleep(10)

    result = get_sources(api_key=API_key)
    pprint.pprint(result)

