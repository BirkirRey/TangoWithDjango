from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here
#def index(request):
#    return HttpResponse("Rango says hay there partner <br/> <a href='/rango/about/'>About</a>")

def index(request):
	#Construct a dictionary to pass the template engine as its context.
	#Note the key boldmessage  is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use
	return render(request, 'rango/index.html', context=context_dict)

#def about(request):
#    return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>Index</a>")

def about(request):
	context_dict = {'developer':'Birkir Reynisson','MEDIA_URL':settings.MEDIA_URL}

	return render(request, 'rango/about.html', context=context_dict)

