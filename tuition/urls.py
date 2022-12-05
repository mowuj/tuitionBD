from django.urls import path
from .views import *
app_name='tuition'
urlpatterns = [
    path('home/', home, name='home'),
    # path('contact/',contact, name='contact'),
    path('search/', search, name='search'),
    path('filter', filter, name='filter'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('post/',postView,name='posts'),
    path('subject/', subjectView, name='subject'),
    path('postlist/', PostListView.as_view(), name='postlist'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='postdetail'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', PostEditView.as_view(), name='edit'),
    # path('create', postCreate, name='create'),
    path('create/', PostCreateView.as_view(), name='create')
]
