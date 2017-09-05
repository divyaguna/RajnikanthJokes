from django.http import HttpResponse
import urllib3
import json



def index(request):
	http = urllib3.PoolManager()
	r = http.request('GET',"http://api.icndb.com/jokes/random?firstName=Rajinikanth")
	data = json.loads(r.data)
	return HttpResponse(data['value']['joke'])
