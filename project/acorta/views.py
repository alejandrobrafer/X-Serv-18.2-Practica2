from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from acorta.models import URL

# Create your views here.

PRACTICE_NAME = "<head><title>URL shortener 2~SARO_2018</title></head>"
PREFIX = 'http://'

port = 8000
machine = "localhost"

def redirection(url):
	return ("<html>" + PRACTICE_NAME + "<head><META HTTP-EQUIV='REFRESH' CONTENT='5;URL=" + str(url) + "'>" +
			"</head><body>Redirecting in 5 seconds ...</body></html>")
            
form = """
<h1><font color="darkslategray"><center><u>URL shortener 2 ~ SARO 2018</u></center></font></h1>
<br>
<form action="" method="POST"><input type="text" name="URL" value="" placeholder="Your original URL here"/>
<input type="submit" value="SHORTEN URL"/><input type="reset" value="Reset"></form>
<br><br>
<b><i>List of original and shortened URLs at this time:</i></b>
"""

@csrf_exempt
def stick(request):

	if request.method == 'GET':
		urls = URL.objects.all()
		response = PRACTICE_NAME + form + "<ul>"
		for url in urls:
			response += "/" + str(url.id) + " --> " + url.url + "<br>"
		response += "</ul>"
		return HttpResponse(response) 
	
	elif request.method == 'POST':
		
		# I search if the URL is in the POST body
		p = request.POST
		url = p.get('URL', False)
		if not url:
			return HttpResponseNotFound(PRACTICE_NAME + "<h1><center>Page Not Found!</center></h1>")
		else:
			# Case: If URL hasn't prefix 'http://' or 'https://'
			if url.find('http://', 0, 7) == -1 and url.find('https://', 0, 8) == -1:
				url = PREFIX + url
				# Note: I have considered that a URL with 'http://'
				# is different that a URL with 'https://'
			
			# I search if the URL is in the dictionary
			try:
				url = URL.objects.get(url=url)
			except URL.DoesNotExist:
				new = URL(url = url)
				new.save()
			
			links = ("<h2><font color='darkslategray'>Choose one:</font></h2>" +
						"<h4>Your shortened URL: <a href='//" + str(machine) + ":" + str(port) + "/" + str(URL.objects.get(url=url).id) +
						"'>http://" + str(machine) + ":" + str(port) + "/" + str(URL.objects.get(url=url).id) + "</a>"
						"<br>Your original URL: <a href='" + str(url) + "'>" +
						str(url) + "</a></h4>")		
		
			return HttpResponse(PRACTICE_NAME + links) 
	else:
		return HttpResponseNotFound(PRACTICE_NAME + "<h1><center>Page Not Found!</center></h1>")
	
def router(request, value):
	try:	
		url = URL.objects.get(id=value)
		return HttpResponse(redirection(url))
	except URL.DoesNotExist:
		return HttpResponseNotFound(PRACTICE_NAME + "<h1><center>Page Not Found!</center></h1>")
