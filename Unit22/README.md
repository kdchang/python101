# OpenCook

# 表單處理

1. 用 HTML 刻個 form
2. 處理 HTTP POST request
3. 檢查表單欄位內容是否正確
4. 把確認過的資料存進 database 當中

# 環境設定

1. $ django-admin startproject opencook
2. $ cd opencook
3. $ python manage.py startapp mainapp
4. $ python manage.py migrate

<script type="text/javascript"> 
  var xhr = new XMLHttpRequest();

  xhr.open('GET', 'http://localhost:8000/api/recipes');

  xhr.send();

  xhr.onload = onHandle

  function onHandle() {
    var data = JSON.parse(JSON.parse(xhr.responseText).data);
    var result = document.getElementById('result');
    var strHTML = '';
    data.forEach(function(value) {
      strHTML += '<div class="col-md-4"><h4>' + value.fields.title  + '</h4><a href="#" class="thumbnail">' + '<img src="' + value.fields.image_path + '">' + '</a></div>'
      result.innerHTML = strHTML;
      console.log(value.fields.image_path);
    });
  }
</script>

from .models import Recipe
from django.http import JsonResponse
from django.core import serializers
import json
# Create your views here.
def get_recipes_api(request):
	recipes = Recipe.objects.all()
	data = serializers.serialize('json', recipes)
	return JsonResponse({ 'data' : data })

url(r'^api/recipes$', get_recipes_api),
from recipe.views import get_recipes_api

<!--       {% for recipe in recipes %} 
      <div class="col-md-4">
        <h4>{{ recipe.title }}</h4>
        <a href="#" class="thumbnail">
          <img src="{{ recipe.image_path }}" alt="">
        </a>
        <p>{{ recipe.created_at | date:"Y / m / d" }}</p>
      </div>
      {% endfor %} -->

appdirs (1.4.3)
dj-database-url (0.4.2)
dj-static (0.0.6)
Django (1.10.6)
gunicorn (19.7.1)
packaging (16.8)
pip (9.0.1)
psycopg2 (2.7.1)
pyparsing (2.2.0)
setuptools (34.3.2)
six (1.10.0)
static3 (0.7.0)
wheel (0.29.0)