# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from Chess.forms import *
from Chess.models import *

import json, decimal, datetime

def create(request):
	#a better way to retrieve data is needed when we get a gazillion wells
	#ideas: apply filters with '|', 
	if request.method == 'POST':
		form = CreateGameForm(request.POST)

		if form.is_valid():
			white = form.cleaned_data['creator']
			name = form.cleaned_data['name']
			
			game = Game(name=name, white=white, status="wait")

			try:
				game.save()
			except IntegrityError:
				#raises this if id and key is not unique
				return HttpResponse('error')

			return HttpResponse('Secret key is %s' % secret_key) # Redirect after POST
	else:
		form = CreateGameForm()

	context = {'form': form}

	return render(request, 'create.html', context)

def lobby(request):
	return

def game(request):
	return

def testing(request):
	return render(request, 'chess.html')

#-----------------AJAX API------------------
@csrf_exempt #dont use this in production!
def recieveCommand(request):
	POST = request.POST
	command =  POST['command']

	return HttpResponse('pass')


#----------------Backend Functions--------------
def parseCommand(command):

