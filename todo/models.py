from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

class TodoQuerySet(models.QuerySet):
  def todos_for_user(self, user):
    return self.filter(
         Q(user=user) # Q makes it an object
      )

  def active(self):
    return self.filter(
        Q(complete=False)
      )

class Todo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  complete = models.BooleanField(default=False)
  target_date = models.DateField()
  date_added = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)

  objects = TodoQuerySet.as_manager() # lets me user the query set

  def __str__(self):
      return "{0}".format(self.name)
