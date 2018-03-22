from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cropselection/', views.cropselection, name='cropselection'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('feedback/', views.feedback, name='feedback'),
    path('state/', views.state, name='state'),
    path('sugarcanefarming/', views.sugarcanefarming, name='sugarcanefarming'),
    path('statecrop/', views.state, name='statecrop'),

]
