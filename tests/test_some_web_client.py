from web_client import SomeResourseClient
import responses
from datetime import datetime

@responses.activate
def test_some_web_client():
    valid_json_answer = {
        "lastActionTime": 1718489808,
        "timeDiff": 1318
    }
    responses.add(method=responses.GET, UTRL='https://www.avito.ru/web/2/user/get-status/d1ccf313d11f83548e6685db2a5aacc2',
                  json=valid_json_answer, status=200)
    some_resource_client = SomeResourseClient('https://www.avito.ru')
    res = some_resource_client.get_user_last_action_time(1718489808)
    assert res == datetime.fromtimestamp(valid_json_answer['last_action_time'] - valid_json_answer['time_diff'])