from django.shortcuts import render

def welcome(request):
  return render(request, "pyTodoList/welcome.html")