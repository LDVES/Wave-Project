from django.urls import path
from .views import PostsList
#Namespace for quests manager
app_name='posts'
urlpatterns = [
	path('', PostsList.as_view(), name='list'),
]