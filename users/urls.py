
from django.urls import path
from users import views

urlpatterns = [
    path('hello', views.HelloView.as_view(), name='hello'),
    path('swap', views.SwapView.as_view(), name='swap'),
    path('move', views.MoveView.as_view(), name='move'),
    path('login', views.User.as_view(), name='login'),
]