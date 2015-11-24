from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import random
from datetime import datetime
time = datetime.now()

def index(request):
	try:
		request.session['gold']
	except:
		request.session['gold']=0
	try:
		request.session['mymessage']
	except:
		request.session['mymessage'] = []
	return render(request, 'turkeykill/index.html')
def attack_turkey(request):
	if request.POST['action'] == 'attack_turkey':
		request.session['damage'] = random.randrange(1,5)
		request.session['hitpoints'] -= request.session['damage']
		result= "Dealt" + str(request.session['damage']) + "to the Turkenator" + str(time)
		request.session['mymessage'].insert(0,str(result))
	return redirect('/')
