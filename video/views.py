from django.shortcuts import render

# Create your views here.

def video_list(request):
 return render(request, 'video_list.html',{})
