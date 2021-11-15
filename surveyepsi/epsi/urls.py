from django.urls import path


from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('<int:grade_code>/', views.detail, name='grade'),
    path('<int:grade_code>/<int:idx>/', views.survey, name='survey'),
    path('<int:grade_code>/<int:idx>/success/', views.success, name='success'),

]