from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("random/", views.random_page, name="random_page"),
    path("add/", views.new_page, name="new_page"),
    path("wiki/<str:title>/edit/", views.edit_entry, name="edit_entry")
]
