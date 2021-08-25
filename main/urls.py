from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    # Home Page
    path('', index , name='index'),
    # Create New Todo 
    path('create/', createNewTodo, name = 'create'),
    # Detail Todo
    path('detail/<todo_id>/', detail, name = 'detail'),
    # Delete Todo
    path('delitte/<todo_id>/', delete , name = "delete"),
    # Update Todo
    path("update/<todo_id>/", update, name = "update"),
]