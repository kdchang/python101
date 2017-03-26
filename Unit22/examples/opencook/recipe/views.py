from django.shortcuts import render
from recipe.models import Recipe
from django.shortcuts import redirect
from django import forms
from django.contrib.auth.decorators import login_required

class RecipeForm(forms.ModelForm):
	class Meta:
		model = Recipe
		fields = ['title', 'image_path', 'description']

# Create your views here.
def get_recipe(request, recipe_id):
	recipe = Recipe.objects.get(pk=recipe_id)
	try:
		if recipe != None:
			return render(request, 'recipe.html', locals())
	except:
		return redirect('/')

def get_recipes(request, type):
	recipes = Recipe.objects.all().order_by('created_at')
	return render(request, 'index.html', locals())

@login_required
def get_create_recipe(request):
	return render(request, 'create_recipe.html')

@login_required
def post_create_recipe(request):
	if request.method == 'POST':
		form = RecipeForm(request.POST)
		if form.is_valid():
			new_recipe = form.save()
			print(new_recipe.pk)
			return redirect('/recipes/' + str(new_recipe.pk))
		else:
			print('false')

	form = RecipeForm()
	return render(request, 'create_recipe.html', locals())