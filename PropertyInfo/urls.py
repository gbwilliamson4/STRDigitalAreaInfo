from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('properties/<uuid:uid>/', views.property_detail, name='property-detail'),
    path('properties', views.property_list, name='property-list'),
    path('add-property/', views.add_property, name='add-property'),
    path('properties/<uuid:uid>/edit', views.edit_property, name='edit-property'),
    path('properties/<uuid:uid>/delete', views.delete_property, name='delete-property'),
    path('<uuid:uid>/', views.property_view, name='property-view'),
    path('properties/<uuid:uid>/add-activity', views.add_activity, name='add-activity'),

    # User Management
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

]
