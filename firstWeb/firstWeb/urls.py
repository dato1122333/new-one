from django.contrib import admin
from django.urls import path

from events.views import(
    add_venue
)

from personal.views import(
    home_screen_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('add_venue/', add_venue, name='add-venue')
]
