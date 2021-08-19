from django.shortcuts import render
from django.views.generic import ListView 
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NameForm


def homepage(request):
    return render(request, 'home.html')



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'forms.html', {'form': form})
    

def new_page(request):
    return HttpResponse("Thank you for filling this form")