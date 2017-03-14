from django.shortcuts import render
from recipe.models import Recipe
from django.shortcuts import redirect
from django import forms

class RecipeForm(forms.ModelForm):
	class Meta:
		model = Recipe
		exclude = ['id', 'created_date']

# Create your views here.
def get_recipe(request, recipe_id):
	recipe = Recipe.objects.get(id=recipe_id)
	try:
		if recipe != None:
			return render(request, 'recipe.html', locals())
	except:
		return redirect('/')

def get_create_recipe(request):
	return render(request, 'create_recipe.html')

def post_create_recipe(request):
	if request.method == 'POST':
		form = RecipeForm(request.POST)
		if form.is_valid():
			new_recipe = form.save()
			return redirect('/recipes/' + new_recipe.id)

	form = RecipeForm()
	return render(request, 'create_recipe.html', locals())