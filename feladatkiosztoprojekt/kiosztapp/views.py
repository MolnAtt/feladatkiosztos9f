from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	kontextus = {"w":5}
	return render(request, "kioszthtml.html", kontextus) # latter is the context