from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StatusWidget, AboutWidget
from .forms import *
from .models import *
from OBS.settings import MEDIA_ROOT, STATIC_ROOT
import os

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
                  {"title":"Админ панель OBS", "text_head":"Панель управления виджетами OBS",
                   "form_widget":form, "files":database})



def open_widget(request, name_slug):
    database = OBS_Model.objects.get(slug=name_slug)
    OBS_Model.objects.filter(slug=name_slug).update(status=True)
    return  render(request, 'Main_OBS/Widget.html',
                   {"title":"Виджет ОБС",
                    "info":database.file,
                    "slug":database.slug,
                    "title":database.title,
                    "subtitle":database.subtitle})


def delete_widget(request, slug_file):
    file = OBS_Model.objects.get(slug=slug_file)
    file_name = file.file
    file.delete()
    os.remove(os.path.join(str(MEDIA_ROOT),str(file_name)))


def edit_status(request, name_slug):
    file = OBS_Model.objects.get(slug=name_slug)
    if file.status == True:
        OBS_Model.objects.filter(slug=name_slug).update(status=False)
    elif file.status == False:
        OBS_Model.objects.filter(slug=name_slug).update(status=True)


def edit_widget(request):
    try:
        name_widget = request.POST.get("name")
        title_widget = request.POST.get("title")
        subtitle_widget = request.POST.get("subtitle")
        OBS_Model.objects.filter(name=name_widget).update(title=title_widget,subtitle=subtitle_widget)
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=400)


class CheckStatus(APIView):
    def get(self,request, name_slug):
        database = OBS_Model.objects.get(slug=name_slug)
        serializer = StatusWidget(database)
        return Response(serializer.data)


class ShowInfo(APIView):
    def get(self, request, name_slug):
        database = OBS_Model.objects.get(slug=name_slug)
        serializer = AboutWidget(database)
        return Response(serializer.data)





