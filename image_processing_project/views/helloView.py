from django.shortcuts import render

def helloWorld(request):
    return render(request, "hello/hello.html")