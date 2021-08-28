from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='index'),
    path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('edit/<int:pk>/', views.RecipeUpdateView.as_view(), name='recipe_update'),
]


# • '/delete/:id' - delete recipe page
# • '/details/:id' - recipe details page
