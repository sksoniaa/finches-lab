from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from the ./models import Finch
from .models import Finch, Toy
from .forms import FeedingForm



def home(request):
	finches = Finch.objects.all()
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')



def assoc_toy(request, finch_id, toy_id):
	print(finch_id, toy_id )
	finch = Finch.objects.get(id=finch_id)
	finch.toys.add(toy_id)# adding a row to our through table the one with 2 foriegn keys in sql
	return redirect('detail', finch_id=finch_id)

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


# cat_id comes from the path in the urls.py 
# path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
def finches_detail(request, finch_id):
	# tell the model to find the row that matches cat_id from the request in the database
	finch = Finch.objects.get(id=finch_id)
	id_list = finch.toys.all().values_list('id')
	# Now we can query the toys table for a the toys 
	# that are not in the id_list!     field looksup in django (google this)
	toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)

	# instatiate the feeding form class to create an instance of the class
	# in otherwords a form object
	feeding_form = FeedingForm()
	return render(request, 'finches/detail.html', {
		'finch': finch,
		'feeding_form': feeding_form,
		'toys': toys_finch_doesnt_have

	})

# 'cats/<int:cat_id>/add_feeding/'
def add_feeding(request, finch_id):
	# process the form request form the client
	form = FeedingForm(request.POST)
	# request.POST is like req.body, its the contents of the form
	# validate the form
	if form.is_valid():
		# create an in memory instance (on django) of our data
		# to be added to psql, commit=False, don't save to db yet
		new_feeding = form.save(commit=False)
		# now we want to make sure we add the cat id to the new_feeding
		new_feeding.finch_id = finch_id
		new_feeding.save() # this is adding a feeding row to the feeding table in psql
	return redirect('detail', finch_id=finch_id) #cat_id is the name of the param in the url path, 
	# cat_id, is the id of the cat from the url request

class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'