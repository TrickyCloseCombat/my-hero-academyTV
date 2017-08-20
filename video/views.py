from django.shortcuts import render
from django.utils import timezone
from .models import Video

# Create your views here.

def video_list(request):
 videos = Video.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
 return render(request, 'video_list.html',{'videos':videos})

