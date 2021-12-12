import requests
import json

def send_sms(number, message):
	url="https://www.fast2sms.com/dev/bulkV2"
	params={
		'authorization':'fc2xWDr1E6sZbjLuPUyXqRBJY7n9m8aA4wGVh5zkSoNOI0TtFgJfuWtdFVMvPK8gNxbTzE1mj4GlUCLw',
		'sender_id':'FSTSMS',
		'message':message,
		'language':'english',
		'route':'p',
		'numbers': number


	}

	response=requests.get(url,params=params)
	dic=response.json()
	print(dic)



send_sms("8988900778","Hey!! there")