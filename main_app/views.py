from django.shortcuts import render

from .models import Finch

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

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

