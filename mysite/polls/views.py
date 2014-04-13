from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.views import generic
from models import Poll
from django.utils import timezone

# Create your views here.

#def index(request):
    #poll = get_object_or_404(Poll, pk=12)
#    return HttpResponse("Hello, world. You're at the poll index.")
#    return render_to_response('index.html')
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'
    def get_queryset(self):
        #return Poll.objects.order_by('-pub_date')[:5]
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Poll.objects.filter(pub_date__lte=timezone.now())

#class ResultsView(generic.DetailView):
#    model = Poll
#    template_name = 'polls/results.html'
