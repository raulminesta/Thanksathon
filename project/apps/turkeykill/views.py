from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import random
from datetime import datetime
time = datetime.now()

def index(request):
	try:
		request.session['hitpoints']
	except:
		request.session['hitpoints']=50
	try:
		request.session['mymessage']
	except:
		request.session['mymessage'] = []
	if request.session['hitpoints'] <= 0:
		return render(request, "turkeykill/victory.html")
	return render(request, 'turkeykill/index.html')
def attack_turkey(request):
	if request.POST['action'] == 'attack_turkey':
		request.session['damage'] = random.randrange(1,5)
		request.session['hitpoints'] -= request.session['damage']
		request.session['turkey'] = random.randrange(0,101)
		result = "Dealt" + ' ' + str(request.session['damage']) + ' ' + "to the Turkenator" + ' ' + str(time)
		request.session['mymessage'].insert(0, str(result))
		if request.session['turkey'] < 4:
			return render(request, 'turkeykill/lost.html')
	return redirect('/')
def reset(request):
	request.session.clear()
	return redirect('/')
