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
    return render(request, 'index.html')
    # return HttpResponse("Home")

# these functions are Lying the piplines


def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
               <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
               <a href="https://www.facebook.com/">Facebook</a><br>
               <a href="https://www.flipkart.com/">Flipkart</a><br>
               <a href="https://www.hindustantimes.com">News</a><br>
               <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)


def analyze(request):
    dj_text = request.GET.get('text', 'defaull')
    cap_fist = request.GET.get('cap_first', 'off')
    print(cap_fist)
    print(dj_text)

    return HttpResponse("captilize first")
