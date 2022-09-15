from django.urls import path
from .views import BookDelete, BookView, BookCreate, BookUpdate, UserLoginView, BookDetail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', BookView.as_view(), name='books'),
    path('book-create/', BookCreate.as_view(), name='book-create'),
    path('book/<slug:pk>/', BookDetail.as_view(), name= 'book'),
    path('book-update/<slug:pk>/', BookUpdate.as_view(), name='book-update'),
    path('book-delete/<slug:pk>/', BookDelete.as_view(), name='book-delete'),
]
