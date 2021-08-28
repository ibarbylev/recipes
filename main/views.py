from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from recipes.models import Recipe


def home_page(request):
    is_recipes = Recipe.objects.exists()
    recipes = []
    if is_recipes:
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


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'edit.html'


class RecipeDeleteView(DeleteView):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'delete.html'


class RecipeDetailView(DetailView):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context['recipe']
        ingredients_str = recipe.ingredients
        ingredients = ingredients_str.split(',')
        context['ingredients'] = ingredients
        # context['heading_text'] = f'Creating of {note.doc_name}'
        # context['description'] = f'On this page you can update the document {note.doc_name}.'
        return context
