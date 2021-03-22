from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signups', views.signups, name='signups'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('feedback', views.feedback, name='feedback'),
    path('contact', views.contact, name='contact'),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('edit/<int:id>', views.edit),
    path('deletecontact/<int:id>', views.deletecontact),
    path('updatecontact/<int:id>', views.updatecontact),
    path('editcontact/<int:id>', views.editcontact),
]
