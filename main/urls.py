from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='index'),
    path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
]


# • '/create' - create recipe page
# • '/edit/:id' - edit recipe page
# • '/delete/:id' - delete recipe page
# • '/details/:id' - recipe details page
