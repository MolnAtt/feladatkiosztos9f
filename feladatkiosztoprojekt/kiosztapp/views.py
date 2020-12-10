from django.shortcuts import render

from .models import Tetel, Tanulo, Valasztott;

# Create your views here.

def home_view(request, *args, **kwargs):
	print('--------------- views.home_view -----------------')

	if request.method == "POST":
		print("ez egy post request")

		valaszto_tanulo = ""
		valasztott_tetel = ""

		megjeloltnevutanulok = Tanulo.objects.filter(tanev=request.POST['user'])
		if len(megjeloltnevutanulok)>0 and megjeloltnevutanulok[0].jelszo == request.POST['pwd']:
			valaszto_tanulo = megjeloltnevutanulok[0]

			print("valóban van ilyen felhasználó")

			print(f'Ezt választotta: {list(request.POST.keys())[3]}')
			valasztott_tetelnev = list(request.POST.keys())[3]
			valasztott_tetel = Tetel.objects.get(tenev = valasztott_tetelnev)

			Valasztott.objects.create(tanuloid = valaszto_tanulo, tetelid = valasztott_tetel)


		else:
			print("nincs ilyen felhasználó vagy van felhasználó, de nem ez a jelszava")


	lista = []

	for t in Tetel.objects.all():
		szures = Valasztott.objects.filter(tetelid = t)
		if len(szures)>0:
			lista.append([t.tenev, szures[0].tanuloid.tanev])
		else:
			lista.append([t.tenev, "nincs"])
		print(f'{t.tenev} tetelnév hozzáadva a lista listához')
		
	kontextus = {"lista": lista}

	return render(request, "kioszthtml.html", kontextus) # latter is the context
