import json 

def parsing(log: str) -> dict:
    keys = ['date', 'level']
    values = log.split('|')

    part1 = {key: value for key, value in zip(keys, values[:2])}
    part2 = dict((el.split('=') for el in values[2].split()))

    for key, value in part2.items():
        if value.isdigit():
            part2[key] = int(value)

    ans = part1 | part2

    return ans

def j_s_o_n(logs: list[str], need_json: bool = True) -> dict:
    parsed_logs = list(parsing(log) for log in logs)

    if need_json:
        with open('logs.json', 'w') as json_file:
            json.dump(parsed_logs, json_file, indent=4, ensure_ascii=False)
    
    return parsed_logs

def filter_logs(logs: list[str], **kwargs) -> list:
    parsed_logs = list(parsing(log) for log in logs)

    ans = list()
    for log in parsed_logs:
        if all(log.get(key) == value for key, value in kwargs.items()):
            ans.append(log)

    return ans

def aggregations(logs: list[str], **kwargs) -> list:
    filtered_logs = filter_logs(logs, **kwargs)

    return len(filtered_logs)

def amount_count(logs: list[str]) -> list:
    filtered_logs = filter_logs(logs, status='fail')

    return sum(log.get('amount') for log in filtered_logs if log.get('amount') is not None)


logs = [
    "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
    "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
    "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
    "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
    "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
]


