from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.signup,name='signup'),
    path('signup/customer/', views.customer_signup,name='customer_signup'),
    path('signup/author/', views.author_signup,name='author_signup'),
    
]