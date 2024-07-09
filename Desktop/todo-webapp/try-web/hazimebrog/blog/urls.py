from django.conf import settings
from django.conf.urls.static import static

from django.urls import path,include

from blog.views import frontpage, post_detail

from . import views

from .views import create_post



urlpatterns = [
    path("", frontpage, name="frontpage"),
    path('blog/<int:blog_id>/review/', views.CreateReviewView.as_view(), name="review"),
    path('create/', create_post, name='create_post'),
    path("<slug:slug>/", post_detail, name="post_detail"),
    path('blog/<int:pk>/delete/', views.DeleteBlogView.as_view(), name='delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)