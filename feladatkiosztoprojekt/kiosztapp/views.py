from django.shortcuts import render

from .models import Tetel, Tanulo, Valasztott;

# Create your views here.

def home_view(request, *args, **kwargs):
	print('--------------- views.home_view -----------------')

	lista = []

	for t in Tetel.objects.all():
		szures = Valasztott.objects.filter(tetelid = t)
		if len(szures)>0:
			lista.append([t.tenev, szures[0].tanuloid.tanev])
		else:
			lista.append([t.tenev, "szabadon választható"])
		print(f'{t.tenev} tetelnév hozzáadva a lista listához')
		
	kontextus = {"lista": lista}
	return render(request, "kioszthtml.html", kontextus) # latter is the context