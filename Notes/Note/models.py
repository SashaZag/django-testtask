from django.db import models

class Note(models.Model):
	text = models.TextField()
	uniq_word_number = models.IntegerField()