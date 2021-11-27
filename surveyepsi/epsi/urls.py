from django.urls import path


from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('<grade>/', views.detail, name='grade'),
    path('<grade>/<int:idx>/', views.survey, name='survey'),
    path('<grade>/<int:idx>/success/', views.success, name='success'),

]