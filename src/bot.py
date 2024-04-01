
import requests
import os


def send_msg(msg: str):
    token = os.environ['GOMU_BOT_TOKEN']
    chanel_id = os.environ['GOMU_CHANEL_ID']

    baseurl = "api.telegram.org"
    url = f"{baseurl}/bot{token}"
    payload = dict(chat_id=chanel_id, text=msg)

    try:
        requests.post(url=url, params=payload)
        raise Exception()
    except Exception as exc:
        print(type(exc))
