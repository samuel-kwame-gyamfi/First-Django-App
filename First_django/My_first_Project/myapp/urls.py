from django.urls import path
from . import views
urlpatterns = [
    # path("greetings",views.hello)
    path("<day>",views.hello)
]