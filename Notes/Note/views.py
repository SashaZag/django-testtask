from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Note


def view_all(request):
	all_notes = Note.objects.order_by('-uniq_word_number')
	return render (request, 'note/viewall.html', {'all_notes': all_notes})

def add_new (request):
	if request.method == 'POST':
		n = Note()
		n.text = request.POST['text']
		text = request.POST['text']
		words = text.split(" ")
		uniq_word_number = len(set(words))
		n.uniq_word_number = uniq_word_number
		n.save()
		all_notes = Note.objects.order_by('-uniq_word_number')
		return HttpResponseRedirect ('/Note')
	else:
		return render(request, 'note/addnew.html')


