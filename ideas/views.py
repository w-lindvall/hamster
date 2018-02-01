from django.shortcuts import render

from ideas.models import Idea, Medium


def index(request):
    recent_ideas = Idea.objects.order_by('-created_at')[:5]
    medium_list = Medium.objects.order_by('name')
    context_dict = {'recent_ideas': recent_ideas, 'medium_list': medium_list}
    return render(request, 'ideas/index.html', context_dict)