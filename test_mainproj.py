from ps.py import basic_url
from ps.py import headers

def test_post_new_pet():

	payload = {'category' : {'id':'0', 'name' :'string'},'name':'doggie', 'photoUrls':['string'], 'tags' :[{'id' :'0', 'name' :'string'}], 'status' :'available'}

	response = requests.post(url = basic_url, headers = headers, data = json.dumps(payload))
	response_body = response.json()
	print(response)
	assert response.status_code == 200
