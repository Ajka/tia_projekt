from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from salon.models import Salon, Service, UserProfile, Reservation, Comments
from salon.forms import UserForm, CommentForm
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User

def index(request):
    salons_list = Salon.objects.all()
    #output = ', '.join([p.name for p in salons_list])
    template = loader.get_template('salons/index.html')
    context = RequestContext(request, {
        'salons_list': salons_list,
    })
    return HttpResponse(template.render(context))

def detail(request, salon_id):
    s = Salon.objects.get(pk=salon_id)
    services = Service.objects.filter(salon=s).order_by("title")
    #template = loader.get_template('salons/detail.html')
    #except Question.DoesNotExist:
     #   raise Http404("Question does not exist")
    return render(request, 'salons/detail.html', {'salon': s,'services':services})

    #return HttpResponse("You're looking at %s." % salon_id)


def service(request, salon_id, service_id):
    s = Service.objects.get(pk=service_id)
    comments = Comments.objects.filter(service=s).order_by("date")
    u=request.user.id

    # template = loader.get_template('salons/detail.html')
    #except Question.DoesNotExist:
    #   raise Http404("Question does not exist")
    if request.method == 'POST':
        form = CommentForm(data=request.POST)

        if form.is_valid():
            c = Comments()
            c.service = s
            c.user = request.user
            c.content_text = form.data['text']
            c.date = datetime.now()
            c.save()


        else:
            print form.errors
    else:
        form = CommentForm()


    return render(request, 'salons/service.html', {'service': s, 'comments': comments,'form':form,'uid':u})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.groups.add(1)
            user.save()
            registered = True
        else:
            print user_form.errors

    else:
        user_form = UserForm()


    return render(request,'salons/register.html', {'user_form': user_form, 'registered': registered} )      


def user_login(request):

    if request.method == 'POST':
  
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
     
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/salon/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        
        return render(request, 'salons/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/salon/')        




    