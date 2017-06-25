import requests


def scrape():
	restaurants = []

	# category = 2
	payload = {
		'entity_id': 1,
		'entity_type': 'city',
		# 'category': category,
		'start': 0,
		'count': 20
	}

	headers = {'Accept':'application/json','user-key': '44c64017dd6335db7da37355e391c64d'}

	raw_results = requests.get('https://developers.zomato.com/api/v2.1/search', params=payload, headers=headers)
	results=raw_results.text
	# print results
	total=raw_results.json()['results_found']
	# total=raw_results.json()
	# print total

	iters = int(total / 20) + 1
	print iters
	for i in range(iters):
		# payload['category'] = category
		payload['start'] = (i*20)
		payload['count'] = 20

		response = requests.get('https://developers.zomato.com/api/v2.1/search', params=payload, headers=headers).json()['restaurants']
		# restaurants = restaurants + response['restaurants']
		print response
		f = open('a.txt','a')
		f.write(str(response))

scrape()
