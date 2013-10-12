# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from Chess.forms import *
from Chess.models import *

import nltk

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

	data={'move': move_string,
			'id_field': move.id
			}


	json_data = json.dumps(data, cls=CustomEncoder)

	return HttpResponse(json_data, content_type='application/json')

@csrf_exempt #dont use this in production!
def validateMove(request):
	move = Move.objects.latest()

	move_string=move.before+'-'+move.after

	data={'move': move_string}


	json_data = json.dumps(data, cls=CustomEncoder)

	return HttpResponse(json_data, content_type='application/json')



#----------------Backend Functions--------------
def parseCommand(data):
	tokens = nltk.word_tokenize(data['command'])
	color = data['color']
	before = list(tokens[0])
	after = list(tokens[-1])

	p1 = chr(96 + before[0]) + before[1]
	p2 = chr(96 + after[0]) + after[1]

	if str(tokens[0])==int and type(tokens[1])==int:
		move = Move(before=p1, after=p2, color=color, status='pending')
		move.save()

		return True
	else: 
		return False