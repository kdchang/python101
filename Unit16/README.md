# 單元16 - 課後專題：OpenCook 食譜分享社群網站開發實務

## Setup
1. 安裝虛擬環境套件
`$ pip3 install virtualenv`
2. 建立虛擬環境
`$ virtualenv venv`
3. 進入虛擬環境
`$ source venv/bin/activate`
4. 安裝 Django-1.10
`$ pip3 install django`
5. 初始化 Django 專案
`$ django-admin.py startproject opencook`
6. 移動到資料夾
`$ cd opencook`
7. 啟動測試伺服器
`$ python3 manage.py runserver`
8. 打開瀏覽器（http://localhost:8000/），觀看成果！

## Views / URL
1. 建立 App
`$ python manage.py startapp recipe`

## Templates

## Model
`$ python manage.py makemigrations`
`$ python manage.py migrate`
