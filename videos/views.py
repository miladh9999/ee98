from django.shortcuts import render, get_object_or_404
from .models import Professor


def home(request):
    professors = Professor.objects.all()
    return render(request, 'videos/home.html', {'professors': professors})


def professor(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    videos = professor.videos.all()
    return render(request, 'videos/professor_page.html', {'professor': professor, 'videos': videos})
