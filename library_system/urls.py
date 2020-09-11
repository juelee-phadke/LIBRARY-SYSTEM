from django.urls import path
from . import views

app_name = 'library_system'
urlpatterns = [
    path('', views.index, name='index'),
    path('roleselect/',views.role,name='role'),
    path('stafflogin/',views.stafflogin,name='stafflogin'),
    path('studentlogin/',views.studentlogin,name='studentlogin'),
    path('staffactions/',views.staffactions,name='staffactions'),
    path('studentactions/<int:studentID>',views.studentactions,name='studentactions'),
    path('borrowbook/<int:studentID>',views.borrowbook,name='borrowbook'),
    path('returnbook/<int:studentID>',views.returnbook,name='returnbook')
]