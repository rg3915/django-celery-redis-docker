from django.urls import path
from myproject.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('task/print_numbers/', v.run_task, name='run_task'),
]
