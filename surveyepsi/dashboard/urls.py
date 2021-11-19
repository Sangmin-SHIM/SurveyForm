from django.urls import path


from . import views



urlpatterns=[
    path('',views.index, name='index2'),
    path('<int:grade_code>/', views.detail, name='grade2'),
    path('<int:grade_code>/<int:idx>/', views.result, name='result2'),
    path('<int:grade_code>/<int:idx>/comment', views.result_comment, name='result2_comment'),

]