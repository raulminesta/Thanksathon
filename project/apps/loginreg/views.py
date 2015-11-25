from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
def index(request):
	# if response['status'] == 'connected':
	# 	return render(request, ('turkeykill/index.html'))
	# else:
	# 	# flash("login not acceptable.")
	# 	return redirect('/')
	return render(request, 'loginreg/index.html')

# def login(request, status):
# 	if status == 'connected':
# 		return render(request, ('turkeykill/index.html'))
# 	else:
# 		flash("login not acceptable.")
# 		return redirect('/')