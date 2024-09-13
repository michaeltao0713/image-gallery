from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('serve_image/<path:file_path>/', views.serve_image, name='serve_image'),
    # path('image/<int:image_id>/', views.image_detail, name='image_detail'),
    path('<int:image_id>/', views.image_list, name='image_detail'),
    path('changes/', views.change_list, name='change_list'),
    path('changes/<int:change_id>/', views.handle_change, name='handle_change'),
]
