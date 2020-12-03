from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
	kontextus = {"lista":
		[
			["1. Tétel", "Fodor Dániel"], 
			["2. Tétel", "üres"]
		] 
		}
	return render(request, "kioszthtml.html", kontextus) # latter is the context