import requests

def test_get_index_req_status_is_200(index_url):
    sucess = 200
    res = requests.get(index_url)
    assert res.status_code == sucess