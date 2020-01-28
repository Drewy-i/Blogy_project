from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

# Create your views here.
#posts = [
#  {

 #               'director': 'Quentin Tarantino',
 #              'title': 'Pulp Fiction',
 #               'date': 'May 1, 1994',
 #              'content': 'Crime',
 #   },

 #        {
 #
 #              'director': 'Martin Scorsese',
 #               'title': 'Taxi driver',
 #              'date': 'February 8, 1976',
 #               'content': 'Thriller',
 #      },
 #       {
            
 #              'director': 'Christopher Nolan',
 #               'title': 'Interstellar',
 #              'date': 'October 26, 2014',
 #               'content': 'Science Fiction',
 #
 #      }
 #      ]

#These functions are in fact returning what i want the user to see,when they are sent to this route.
#This is just a dummy data now.


def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'movies/home.html',context)

def info(request):
    return render(request,'movies/info.html',{'title':'Info'})