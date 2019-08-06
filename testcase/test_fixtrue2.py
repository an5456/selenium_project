def test_1(topics):
    # json = requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
    assert len(topics['topics']) == 2


def test_2(topics):
    # json = requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
    assert topics['topics'][0]['deleted'] == False