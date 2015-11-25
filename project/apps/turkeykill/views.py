from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import random
from datetime import datetime
from apps.loginreg.models import User, Weapon
time = datetime.now()

def index(request):
	try:
		request.session['hitpoints']
	except:
		request.session['hitpoints']=100000
	try:
		request.session['userpoints']
	except:
		request.session['userpoints'] = 0
	try:
		request.session['mymessage']
	except:
		request.session['mymessage'] = []
	if request.session['hitpoints'] <= 0:
		return render(request, "turkeykill/victory.html")
	weapons= Weapon.objects.all()
	context={
		'weapons': weapons
	}
	return render(request, 'turkeykill/index.html', context)
def attack_turkey(request):
	if request.POST['action'] == 'attack_turkey':
		request.session['damage'] = random.randrange(1,6)
		request.session['hitpoints'] -= request.session['damage']
		request.session['userpoints'] += request.session['damage'] * 5
		request.session['turkey'] = random.randrange(0,101)
		result = "Dealt" + ' ' + str(request.session['damage']) + ' ' + "to the Turkenator" + ' ' + str(time)
		request.session['mymessage'].insert(0, str(result))
		if request.session['turkey'] < 10:
			return render(request, 'turkeykill/lost.html')
	return redirect('/turkeykill')
def weapon_attack(request):
	if request.POST['weapon_attack'] == 'Turkey Baster':
		request.session['damage'] = random.randrange(1,6)
		boosted_attack= (Weapon.objects.get(name='Turkey Baster').damage * request.session['damage'])
		request.session['hitpoints'] -= boosted_attack
		request.session['userpoints'] -= 5
		result = "Dealt" + ' ' + str(boosted_attack) + ' ' + "to the Turkenator" + ' ' + str(time)
		request.session['mymessage'].insert(0, str(result))
	if request.POST['weapon_attack'] == 'Microwave Oven':
		request.session['damage'] = random.randrange(1,6)
		boosted_attack= (Weapon.objects.get(name='Microwave Oven').damage * request.session['damage'])
		request.session['hitpoints'] -= boosted_attack
		request.session['userpoints'] -= 20
		result = "Dealt" + ' ' + str(boosted_attack) + ' ' + "to the Turkenator" + ' ' + str(time)
	if request.POST['weapon_attack'] == 'Carving Knife':
		request.session['damage'] = random.randrange(1,6)
		boosted_attack= (Weapon.objects.get(name='Carving Knife').damage * request.session['damage'])
		request.session['hitpoints'] -= boosted_attack
		request.session['userpoints'] -= 50
		result = "Dealt" + ' ' + str(boosted_attack) + ' ' + "to the Turkenator" + ' ' + str(time)
	if request.POST['weapon_attack'] == 'Bazooka':
		request.session['damage'] = random.randrange(1,6)
		boosted_attack= (Weapon.objects.get(name='Bazooka').damage * request.session['damage'])
		request.session['hitpoints'] -= boosted_attack
		request.session['userpoints'] -= 100
		result = "Dealt" + ' ' + str(boosted_attack) + ' ' + "to the Turkenator" + ' ' + str(time)
	if request.POST['weapon_attack'] == 'Nuke':
		boosted_attack= Weapon.objects.get(name='Nuke').damage
		request.session['hitpoints'] -= boosted_attack
		request.session['userpoints'] = 0 
		result = "Dealt" + ' ' + str(boosted_attack) + ' ' + "to the Turkenator" + ' ' + str(time)
		request.session['mymessage'].insert(0, str(result))
	return redirect('/turkeykill')
def buy_weapons(request):
	return render(request, 'turkeykill/buy_weapons.html')
def reset(request):
	request.session.clear()
	return redirect('/turkeykill')
