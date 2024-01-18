from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home),
    path('',views.list),
    path('add',views.add),
    path('edit/<int:pk>/', views.edit, name='edit_place'),
    path('manage',views.manage),
    path('', list, name='list'),
    path('delete/<int:pk>',views.delete_place),
    path('login',views.custom_login),
    path('logout',views.logout_view),
]