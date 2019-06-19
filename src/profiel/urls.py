from django.urls import path
from . import views


app_name = "profiel"
urlpatterns = [
    path("", views.profiel_lijst, name="profielen-lijst"),
    path("<int:profiel>", views.profiel_detail, name="profielen-detail"),
]
