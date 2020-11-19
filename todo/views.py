from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    # this last items is the items variable we've just created
    return render(request, 'todo/todo_list.html', context)
