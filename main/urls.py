from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = "main"

router = routers.DefaultRouter()
router.register(r'todoes', TodoViewSet)
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
    #django rest_framework
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]