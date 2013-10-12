# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from Chess.forms import *
from Chess.models import *

import nltk
import datetime
import json

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

	if parseCommand(POST): 
		return HttpResponse('pass')
	else: 
		return HttpResponse('fail: invalid command')

@csrf_exempt #dont use this in production!
def getMove(request):
	move = Move.objects.latest()

	move_string=move.before+'-'+move.after

	data={'source': move.before, 
			'target': move.after,
			'id_field': move.id
		}

	json_data = json.dumps(data)

	return HttpResponse(json_data, content_type='application/json')

@csrf_exempt #dont use this in production!
def validateMove(request):
	move_id = request.POST.get('id')
	move = Move.objects.get(id=move_id)
	move['status']=complete

	return HttpResponse('pass')



#----------------Backend Functions--------------
def parseCommand(data):
	tokens = nltk.word_tokenize(data['command'])
	color = data['color']
	before = list(tokens[0])
	after = list(tokens[-1])

	p1 = chr(96 + int(before[0])) + str(before[1])
	p2 = chr(96 + int(after[0])) + str(after[1])

	print('I got here')

	move = Move(before=p1, after=p2, color=color, status='pending',action_time=datetime.datetime.now())
	move.save()

	return True


