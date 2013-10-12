from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length=50)

	white = models.CharField(max_length=50)
	black = models.CharField(max_length=50)

	status = models.CharField(max_length=50)


class Move(models.Model):
	before = models.CharField(max_length=3)
	after = models.CharField(max_length=3)
	color = models.CharField(max_length=1)
	status = models.CharField(max_length=50)

	#game = models.ForeignKey('Game')
	class Meta:
		get_latest_by:"order_date"