from django.urls import include, path
from . import views as v


urlpatterns = [
    path('', v.homepage, name='homepage'),
    path('register', v.RegisterParticipant.as_view(), name='register'),
]
