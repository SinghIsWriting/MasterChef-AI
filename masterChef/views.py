from django.shortcuts import render, redirect
from django.views import View
from masterChef.forms import RecipeForm1, RecipeForm2
from masterChef.masterChefAI import masterChef, masterChefPro

# Create your views here.
class Home(View):
    def get(self, request):
        recipe = request.session.get('master_recipe', '')
        form = RecipeForm1()
        context = {'form': form, 'recipe': recipe}
        return render(request, 'masterChef/home.html', context)
    
    def post(self, request):
        form = RecipeForm1(request.POST)
        if form.is_valid():
            recipe_msg = form.cleaned_data['recipe_msg']
            # print(recipe_msg)
            recipe = masterChef(recipe_msg)
            request.session['master_recipe'] = recipe
        form = RecipeForm1()
        return redirect('/')

class Ingredients(View):
    def get(self, request):
        recipe = request.session.get('master_recipe_1', '')
        form = RecipeForm2()
        context = {'form': form, 'recipe': recipe}
        return render(request, 'masterChef/ingredients.html', context)
    
    def post(self, request):
        form = RecipeForm2(request.POST)
        if form.is_valid():
            recipe_msg = form.cleaned_data['recipe_msg']
            # print(recipe_msg)
            recipe = masterChefPro(recipe_msg)
            request.session['master_recipe_1'] = recipe
        form = RecipeForm2()
        return redirect('ingredients')
