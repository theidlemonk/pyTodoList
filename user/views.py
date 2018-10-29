from django.shortcuts import render
from todo.models import Todo

# Create your views here.
def home(request):
  user = request.user #check if the user if logged in
  # todos = Todo.objects.filter(user = user)
  todos = Todo.objects.todos_for_user(user) #using query set to get all todos for user
  active_todos = todos.active() # using query set to further filter to get active todos
  return render(request, "user/home.html", {"todos": todos, "active_todos": active_todos})