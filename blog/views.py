from django.shortcuts import render
from django.http import HttpResponse


def posts_list(request):
    n = ['Dmytro', 'Masha', 'Olga', 'Kolya']
    return render(request, 'blog/index.html', context={'names': n})
