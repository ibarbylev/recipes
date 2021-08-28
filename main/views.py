from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from recipes.models import Recipe


def home_page(request):
    is_recipes = Recipe.objects.exists()
    recipes = []
    if not is_recipes:
        recipes = Recipe.objects.all()
    context = {
        'is_recipes': is_recipes,
        'recipes': recipes
    }
    return render(request, 'index.html', context)


class RecipeCreateView(CreateView):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('index')


