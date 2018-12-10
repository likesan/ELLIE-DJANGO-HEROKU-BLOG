from django.urls import path
from.import views

# specify this url page below to be called individually.
app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name = "list"),
    path('<slug>/', views.article_detail, name = "detail"),
]