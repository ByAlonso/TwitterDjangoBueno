from django.shortcuts import render
from .funciones import source
from .models import WordList


from django.http import HttpResponse,HttpResponseRedirect
from django.conf.urls import url
# Create your views here.


def PageView(request):
    word_list = WordList.objects.all()
    return render(request, 'index.html',{'word_list' : word_list})

def GetData(request):
    if WordList.objects.all().count() != 0:
        WordList.objects.all().delete()

    try:
        username = request.POST['username']
        twitter_obj = source.Twitter2(username)
        word_list = twitter_obj.word_count()
        word_list = WordList(username= username,content = word_list)
        word_list.save()
    except:
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')

def DeleteData(request):
    WordList.objects.all().delete()
    return HttpResponseRedirect('/')