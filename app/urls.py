
from django.urls import path
from app import views


urlpatterns = [
    path('',views.home,name='home'),
    path("imagepost/<int:id>", views.ImagePost, name="imagepost"),
    path('upload_img/',views.Upload_image,name='upload_img'),
    # path('rotate_left/<int:id>',views.rotateLeft,name='rotate_left'),
]
