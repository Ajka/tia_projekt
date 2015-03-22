from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from salon.models import Salon
from django.template import RequestContext, loader

def index(request):
    salons_list = Salon.objects.all()
    #output = ', '.join([p.name for p in salons_list])
    template = loader.get_template('salons/index.html')
    context = RequestContext(request, {
        'salons_list': salons_list,
    })
    return HttpResponse(template.render(context))

def detail(request, salon_id):
	#try:
    s = Salon.objects.get(pk=salon_id)
    #except Question.DoesNotExist:
     #   raise Http404("Question does not exist")
    return render(request, 'salons/detail.html', {'salon': s.name})

    #return HttpResponse("You're looking at %s." % salon_id)

"""
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)  
"""


    