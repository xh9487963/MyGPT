import os
import requests
import json
import random
import time
import string
from ...typing import sha256, Dict, get_type_hints
import openai

url = "https://wewordle.org/gptapi/v1/android/turbo"
model = ['gpt-3.5-turbo']
supports_stream = False
needs_auth = False

openai.api_key = ''
api_key_list = [""]

def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    base = ''
    for message in messages:
        base += '%s: %s\n' % (message['role'], message['content'])
    base += 'assistant:'

    _user_id = ''.join(random.choices(
        f'{string.ascii_lowercase}{string.digits}', k=16))
    _app_id = ''.join(random.choices(
        f'{string.ascii_lowercase}{string.digits}', k=31))
    
    openai.api_key = api_key_list[int(kwargs['model_detail']) - 1]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "user", "content": base}
        ]
    )
    yield completion.choices[0].message["content"]

    # make current date with format utc
    # _request_date = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())
    # headers = {
    #     'accept': '*/*',
    #     'pragma': 'no-cache',
    #     'Content-Type': 'application/json',
    #     'Connection': 'keep-alive'
    # }
    # data = {
    #     "user": _user_id,
    #     "messages": [
    #         {"role": "user", "content": base}
    #     ],
    #     "subscriber": {
    #         "originalPurchaseDate": None,
    #         "originalApplicationVersion": None,
    #         "allPurchaseDatesMillis": {},
    #         "entitlements": {
    #             "active": {},
    #             "all": {}
    #         },
    #         "allPurchaseDates": {},
    #         "allExpirationDatesMillis": {},
    #         "allExpirationDates": {},
    #         "originalAppUserId": f"$RCAnonymousID:{_app_id}",
    #         "latestExpirationDate": None,
    #         "requestDate": _request_date,
    #         "latestExpirationDateMillis": None,
    #         "nonSubscriptionTransactions": [],
    #         "originalPurchaseDateMillis": None,
    #         "managementURL": None,
    #         "allPurchasedProductIdentifiers": [],
    #         "firstSeen": _request_date,
    #         "activeSubscriptions": []
    #     }
    # }
    # response = requests.post(url, headers=headers, data=json.dumps(data))
    # if response.status_code == 200:
    #     _json = response.json()
    #     if 'message' in _json:
    #         message_content = _json['message']['content']
    #         message_content = message_content.replace('**assistant:** ', '')
    #         yield message_content
    # else:
    #     print(f"Error Occurred::{response.status_code}")
    #     return None


params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join(
        [f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
