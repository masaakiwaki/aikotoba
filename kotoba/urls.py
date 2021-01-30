from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.AikotobaListView.as_view(), name='aikotoba_list'),
    path('aikotoba_create/', views.AikotobaCreateView.as_view(), name='aikotoba_create'),
    path('aikotoba_detail/<slug:pk>/', views.AikotobaDetailView.as_view(), name='aikotoba_detail'),
    path('aikotoba_update/<slug:pk>/', views.AikotobaUpdateView.as_view(), name='aikotoba_update'),
    path('aikotoba_delete/<slug:pk>/', views.AikotobaDeleteView.as_view(), name='aikotoba_delete'),
]