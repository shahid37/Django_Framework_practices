# i have created this file :shahid
from django.http import HttpResponse
from django.shortcuts import render

# these two fun are urls & views k hain

def index(request):
    return HttpResponse('''<h1>hello shahid finally make a simple website waooo</h1> <a href ="https://github.com/shahid37">login  GitHub Account</a>''')


def about(request):
    return HttpResponse("about shahid")

# this function is use templates


def index(request):
    params = {'name': 'ahmed & shahid', 'place': 'Mars'}
    return render(request, 'index.html', params)
    # return HttpResponse("Home")

# these functions are Lying the piplines


def remove_punc(request):
    return HttpResponse("Remove punc")


def cap_first(request):
    return HttpResponse("captilize first")


def new_line_remove(request):
    return HttpResponse("Remove new line")


def space_remove(request):
    return HttpResponse("remove space <a href='/'>Back Button</a>")


def char_count(request):
    return HttpResponse("character count")

