from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('create-user/', SignUpView.as_view(), name='create-user'),
]