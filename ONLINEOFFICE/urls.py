from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name='index'),
    path('Login', views.Loginpage, name='Login'),
    path('Warning', views.Warning, name='Warning'),
    path('Signup', views.Signuppage, name='Signup'),
    path('Logout', views.logoutUser, name='Logout'),
    # path('info', views.information, name='info'),
    path('coordinator', views.coordinator, name='coordinator'),
    path('Request', views.requestpage, name='Request'),
    path('Home', views.Homepage, name='Home'),
    path('Scheduler', views.Schedulerpage, name='Scheduler'),
    path('updatepage2/<str:pk>/', views.updatepage2, name="updatepage2"),
    path('update/<str:pk>/', views.updatepage, name="update"),
    path('delete/<str:pk>/', views.deletepage, name="delete"),
 # path('Adminpagerequest', views.Adminpagerequest, name='Adminpagerequest'),naging coordinator
 #path('Adminpage', views.Adminpage1, name='Adminpage'),naging info
]