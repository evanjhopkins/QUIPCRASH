import requests
import random
import string
import json

def main():
	i=0
	found = False
	while (not found):
		i=i+1
		code = random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_lowercase)
		code = code.upper()
		response = requests.get("http://blobcast.jackboxgames.com/room/"+code+"?userId=024052bf-01b2-4f51-a0ec-542a05c451d1")
		json_obj = json.loads(response.content)

		if 'error' in json_obj:
			print "["+str(i)+"]   " + code + " <-- "+json_obj['error']
		else:
			found = True
			print "FOUND ROOM --> "+code

if __name__ == '__main__':
	main()