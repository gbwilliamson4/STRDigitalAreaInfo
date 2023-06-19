from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import uuid
from django.urls import reverse


def index(request):
    if request.user.is_authenticated:
        return redirect('property-list')
    else:
        return redirect('login')


def property_detail(request, uid):
    property_info = Property.objects.get(uid=uid)
    activity_type = ActivityType.objects.filter(property=property_info)
    activity_info = {}

    for activity in activity_type:
        activities = Activities.objects.filter(activity_type__in=ActivityType.objects.filter(pk=activity.pk))
        activity_info[activity] = activities

    print(activity_info)

    context = {'property': property_info, 'activity_info': activity_info}
    return render(request, 'PropertyInfo/property-detail.html', context)


def property_list(request):
    properties = Property.objects.filter(user=request.user.pk)
    context = {'properties': properties}
    return render(request, 'PropertyInfo/property-list.html', context)


def add_property(request):
    if request.method == 'POST':
        user = request.user
        property_name = request.POST['property_name']
        property_description = request.POST['property_description']
        uid = uuid.uuid4()

        prop = Property(user=user, property_name=property_name, property_description=property_description, uid=uid)
        prop.save()
        activity1 = ActivityType(type="Food", property=prop)
        activity1.save()
        activity2 = ActivityType(type="Shopping", property=prop)
        activity2.save()
        activity3 = ActivityType(type="Entertainment", property=prop)
        activity3.save()
        return redirect('property-list')
    else:

        context = {}
        return render(request, 'PropertyInfo/add-property.html', context)


def edit_property(request, uid):
    if request.method == 'POST':
        user = request.user
        property_name = request.POST['property_name']
        property_description = request.POST['property_description']

        # prop = Property(user=user, property_name=property_name, property_description=property_description)
        prop = Property.objects.get(uid=uid)
        prop.user = user
        prop.property_name = property_name
        prop.property_description = property_description
        prop.save()

        return HttpResponseRedirect(reverse('property-detail',
                                            args=[uid]))
    else:
        property_info = Property.objects.get(uid=uid)
        context = {'property': property_info}
        return render(request, 'PropertyInfo/edit-property.html', context)


def delete_property(request, uid):
    prop = Property.objects.get(uid=uid)
    prop.delete()
    return redirect('property-list')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, "Login Successful.")
            return redirect('index')
        else:
            messages.error(request, 'Invalid username/password combination.')
            return redirect('login')
    else:
        # messages.error(request, 'Problem! Sooo many problems!')
        # return redirect('login')
        return render(request, 'PropertyInfo/login.html', {})


def logout_user(request):
    logout(request)
    # messages.success(request, 'You have been successfully logged out. Please come again soon.')
    return render(request, 'PropertyInfo/logout.html')


def signup(request):
    pass
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #
    #     if form.is_valid():
    #         user = form.save()
    #
    #         login(request, user)
    #         messages.success(request, "Login Successful.")
    #         return redirect('index')
    #
    # else:
    #     form = SignUpForm()
    #
    # context = {'form': form}
    # return render(request, 'PropertyInfo/signup.html', context)


# def property_edit(request):
#     pass


def property_view(request, uid):
    property_info = Property.objects.get(uid=uid)
    property_name = property_info.property_name
    activity_type = ActivityType.objects.filter(property=property_info)
    activity_info = {}

    for activity in activity_type:
        activities = Activities.objects.filter(activity_type__in=ActivityType.objects.filter(pk=activity.pk))
        activity_info[activity] = activities

    # print(activity_info)

    context = {'property': property_info, 'property_name': property_name, 'activity_info': activity_info}

    return render(request, 'PropertyInfo/property-view.html', context)


def add_activity(request, uid):
    # Need to pass through activity types
    if request.method == 'POST':
        property_info = Property.objects.get(uid=uid)
        activity_type = ActivityType.objects.get(type=request.POST['activity_type'], property=property_info)
        location = request.POST['location']
        url = request.POST['url']

        activity = Activities(property=property_info, activity_type=activity_type, location=location, url=url)
        activity.save()
        return HttpResponseRedirect(reverse('property-detail',
                                            args=[uid]))
    else:
        activity_types = ActivityType.objects.filter(property=Property.objects.get(uid=uid))
        context = {'activity_types': activity_types}
        return render(request, 'PropertyInfo/add-activity.html', context)


import qrcode
import qrcode.image.svg
from io import BytesIO


def view_qr(request, uid):
    property_info = Property.objects.get(uid=uid)
    factory = qrcode.image.svg.SvgPathImage
    url = 'http://127.0.0.1:8000/1a05a526-2dc5-42f9-b41b-3e112d0f4f0f/'
    img = qrcode.make(url, image_factory=factory, box_size=20)
    stream = BytesIO()
    img.save(stream)
    # context["svg"] = stream.getvalue().decode()
    context = {'property_info': property_info, 'svg': stream.getvalue().decode()}

    # http://127.0.0.1:8000/1a05a526-2dc5-42f9-b41b-3e112d0f4f0f/

    return render(request, 'PropertyInfo/view-qr.html', context)
