from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

class FinchCreate(CreateView):
	model = Finch
	fields = '__all__'


class FinchUpdate(UpdateView):
	model = Finch
	# disallow renaming of the cat
	fields = ['breed', 'description', 'age']
	# uses def get_absolute_url in models.py to redirect the put request
	# back to the the detail page of the cat just updated

class FinchDelete(DeleteView):
	model = Finch
	# define the success_url here because the def get_absolute_url in the models.property
	# redirects to a detail page which doesn't make sense since we deleted it
	success_url = '/finches' # redirect to cats_index path


def finches_index(request):
	# tell the model to find all the rows in the cats table!
	finches = Finch.objects.all()
	return render(request, 'finches/index.html', {
		'finches': finches
		#'cats' becomes a variable name in 'cats/index.html'
		# just like express 
		# res.render('cats/index', {'cats': cats})
  })

def finches_detail(request, finch_id):
	# tell the model to find the row that matches cat_id from the request in the database
	finch = Finch.objects.get(id=finch_id)
	return render(request, 'finches/detail.html', {
		'finch': finch
		# finch (the key) is the variable name in cats/detail.html 
	})

