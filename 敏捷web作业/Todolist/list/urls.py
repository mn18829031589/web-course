from django.contrib import admin
from django.urls import path
from list import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('creatTodoList/',views.creatTodoList),
    path('deleteTodoList/',views.deleteTodoList),
    path('returnIdTODO/',views.returnIdTODO),
    path('returnAll/',views.returnAll)

]