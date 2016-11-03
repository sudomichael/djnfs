from django.shortcuts import render

# Create your views here.

def movie_list(request):
    return render(request, 'nfs/movie_list.html', {})


