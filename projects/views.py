from django.shortcuts import render,redirect
from .models import News
from .forms import *

# Create your views here.
def home(request):
    all_news = News.objects.all()
    if request.POST:
        news_id = request.POST['one']
        one_news = News.objects.get(id=news_id)
        if request.user in one_news.likes.all():
            one_news.likes.remove(request.user)
        else:
            one_news.likes.add(request.user)
    return render(request, 'home.html', {'all_news': all_news})

def create(request):
    form = NewsForm()
    if request.POST:
        form = NewsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request, 'create.html', {'form': form})