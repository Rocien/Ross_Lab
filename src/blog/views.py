from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home_view(request, *args, **kwargs): # *args, **kwargs
	print(args, kwargs)
	print(request.user)
	# return HttpResponse("<h1>Hello World</h1>") #string of HTML code
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
	my_context = {
  "We love music and we are making it sound as better as possible": "Ford",
  "Ross Lab recods is the future": "We do gospel music, mostly Kompa and Zouk",
  "year": 1964
}
	return render(request, "about.html", my_context)