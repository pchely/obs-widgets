from django.shortcuts import render, redirect
from .forms import *
from .models import *



text_head = "Панель управления виджетами OBS"

def admin_board(request):
    database = OBS_Model.objects.all()
    if request.method == 'POST':
        form = AddWiget(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddWiget()
    return render(request, 'Main_OBS/AdminBoard.html',
                  {"title":"Админ панель OBS", "text_head":text_head,
                   "form_widget":form, "files":database})



def open_widget(request, name_slug):
    database = OBS_Model.objects.get(slug=name_slug)
    print(database.file)
    return  render(request, 'Main_OBS/Widget.html',
                   {"title":"Виджет ОБС",
                    "info":database.file})



