from django.urls import path

from .views import EntryListView,EntryDetail,CreateEntry

urlpatterns = [
    path("", EntryListView.as_view(), name="index"),
    path("wiki/<str:title>/", EntryDetail.as_view(), name="entry_detail"),
    path("create_entry/", CreateEntry.as_view(), name="create-entry")
]
