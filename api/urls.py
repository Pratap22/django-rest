from django.urls import path, include
from .views import BookAPIView

urlpatterns = [
    path('books/', BookAPIView.as_view()),
    path('todos/', include('todos.urls')),
    path('posts/', include('posts.urls')),
]
