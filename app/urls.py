from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import user_profile, profile,searchuser,follow,unfollow

urlpatterns = [
  path('', views.welcome , name='index'),
  path('new/image/', views.upload_image, name='new-image'),
  path('reviews/<int:id>', views.review, name='reviews'),
  path('profile/', views.profile, name='profile'),
  path('user_profile/<username>/', user_profile, name='user_profile'),
  path('profile/', profile, name='profile'),
  path('search/',searchuser ,name='searchuser'),
  path('follow/<pk>', follow, name='follow'),
  path('unfollow/<pk>',unfollow, name='unfollow'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)