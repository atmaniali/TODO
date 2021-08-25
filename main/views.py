from django.shortcuts import get_object_or_404, render, redirect
from .forms import * 
from .models import *
from django.contrib import messages

# Create your views here.
# home page view
# @params object : contiens all object of Todo model 
def index(request):
    template_name = 'main/home.html'
    context = {}
    object = Todo.objects.all()
    print(object)
    context['objs'] = object
    return render(request, template_name, context)

# create new todo view
#@parms : form is form where stock todo models in BD
#         context[form] : pass formulaire in html template
def createNewTodo( request):
    template_name = 'main/create.html'
    context = {}
    form =  TodoForm(request.POST or None)   
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'you have create todo with succes')
            return redirect('main:create')
    context['form'] = form
    return render(request, template_name, context) 
# detail view
# @params : object  its stock the object where pk is equale to 'todo_id'
def detail(request, todo_id):
    """  
    this view for show detail of Todo Object givin by id
    """
    template_name = 'main/detail.html'    
    context = {}
    object  = get_object_or_404(Todo, pk = todo_id)
    context['object'] = object
    return render(request, template_name, context)  
# delete view
# @params : object  its stock the object where pk is equale to 'todo_id'         
def delete (request, todo_id):    
    """  
    this view for delete Todo Object givin by id
    """
    template_name = 'main/detail.html'    
    context = {}
    object  = get_object_or_404(Todo, pk = todo_id)
    object.delete()
    messages.success(request, 'you have deleted with secces')
    return render(request, template_name, context)
# update view
# @params: object  its stock the object where pk is equale to 'todo_id'
#         context[form] : pass formulaire in html template
def update(request, todo_id):
    """  
    this view for update Todo Object givin by id
    """
    template_name = 'main/update.html'    
    context = {}
    object  = get_object_or_404(Todo, pk = todo_id)
    form = TodoForm(request.POST or None, instance= object)
    if form.is_valid():
        form.save()
        messages.success(request, 'you have update with succes')
        return redirect(request.path)
    context['form'] = form
    return render(request, template_name, context)