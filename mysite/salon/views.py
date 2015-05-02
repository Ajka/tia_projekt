from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from salon.models import Salon, Service, UserProfile, Reservation, Comments
from salon.forms import *
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.datetime_safe import datetime


def index(request):
    salons_list = Salon.objects.all()
    template = loader.get_template('salons/index.html')
    context = RequestContext(request, {
        'salons_list': salons_list,
    })
    return HttpResponse(template.render(context))


def user_info(request):
    u = request.user
    reservations = Reservation.objects.filter(user=u)

    if request.method == 'POST' and "delete" in str(request.POST):
        id = str(request.POST)[int(str(request.POST).index("delete") + 6):]
        number = int(id[:id.index("'")])
        r = Reservation.objects.get(pk=number)
        r.delete()
    sum = 0
    for r in reservations:
        sum += r.service.price

    return render(request, 'salons/user_info.html', {'user': u, 'reservations': reservations, 'sum': sum})


def reserve(request, salon_id, service_id):
    s = Salon.objects.get(pk=salon_id)
    service = Service.objects.filter(salon=s).get(pk=service_id)
    form = ReservationForm()
    reserved = False
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            r = Reservation()
            r.user = request.user
            r.service = service
            r.date = form.data['date']
            r.time = form.data['time']
            r.save()
            reserved = True
    return render(request, 'salons/reserve.html', {'reserved': reserved, 'salon': s, 'service': service, 'form': form})


def detail(request, salon_id):
    s = Salon.objects.get(pk=salon_id)
    services = Service.objects.filter(salon=s).order_by("title")
    # template = loader.get_template('salons/detail.html')
    #except Question.DoesNotExist:
    #   raise Http404("Question does not exist")
    return render(request, 'salons/detail.html', {'salon': s, 'services': services})
    #return HttpResponse("You're looking at %s." % salon_id)


def service(request, salon_id, service_id):
    s = Service.objects.get(pk=service_id)
    salon = Salon.objects.get(pk=salon_id)
    services = Service.objects.filter(salon=salon).order_by("title")
    comments = Comments.objects.filter(service=s).order_by("date")
    u = request.user.id

    # template = loader.get_template('salons/detail.html')
    # except Question.DoesNotExist:
    #   raise Http404("Question does not exist")
    if request.method == 'POST' and 'createComment' in request.POST:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            c = Comments()
            c.service = s
            c.user = request.user
            c.content_text = form.data['text']
            c.date = datetime.now()
            c.save()
            form = CommentForm()

        else:
            print form.errors
    else:
        form = CommentForm()

    if request.method == 'POST' and "delete" in str(request.POST):
        id = str(request.POST)[int(str(request.POST).index("delete") + 6):]
        number = int(id[:id.index("'")])
        com = Comments.objects.get(pk=number)
        com.delete()


    return render(request, 'salons/service.html',
                  {'service': s, 'services': services, 'salon': salon, 'comments': comments, 'form': form, 'uid': u})


def modify(request,salon_id, service_id,comments_id):
    s = Service.objects.get(pk=service_id)
    salon = Salon.objects.get(pk=salon_id)
    services = Service.objects.filter(salon=salon).order_by("title")
    form = CommentForm()
    u = request.user.id
    comments = Comments.objects.filter(service=s).order_by("date")

    if request.method == 'POST':
        content = request.POST['comment_mod']
        old = Comments.objects.get(pk=comments_id)
        s = old.service

        comment = Comments()
        comment.content_text = content
        comment.user = old.user
        comment.service = old.service
        comment.date = datetime.now()
        comment.save()
        old.delete()
        return render(request, 'salons/service.html', {'service': s, 'services': services, 'salon': salon, 'comments': comments, 'form': form, 'uid': u})




    com = Comments.objects.get(pk=comments_id)
    return render(request, 'salons/modify.html', {'comment': com, })
    #return render(request, 'salons/service.html',
     #             {'service': s, 'services': services, 'salon': salon, 'comments': comments, 'form': form, 'uid': u})


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

    return render(request, 'salons/register.html', {'user_form': user_form, 'registered': registered})


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




    