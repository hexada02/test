import requests
import json
from datetime import datetime, timedelta


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_id):
        resp = requests.get(f'{self.url}/web/2/user/get-status/{user_id}')
        json_data = json.loads(resp.text)
        return json_data

    def get_user_last_action_time(self, user_id):
        json_data = self.__user_get_status(user_id)
        time_diff = json_data["timeDiff"]
        time_difference = timedelta(seconds=time_diff)
        last_action_time = datetime.now() - time_difference
        return last_action_time

some_resource_client = SomeResourceClient('https://www.avito.ru')
print(some_resource_client.get_user_last_action_time('d1ccf313d11f83548e6685db2a5aacc2'))
