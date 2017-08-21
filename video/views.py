from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Video

# Create your views here.

def video_list(request):
 videos = Video.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
 return render(request, 'video_list.html',{'videos':videos})

def video_detail(request, pk):
        videos = get_object_or_404(Video, pk=pk)
        return render(request, 'video_detail.html', {'videos': videos})

