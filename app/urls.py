from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/ ', admin.site.urls),
    path('',views.home,name="Hi bro"),
    path('new_user',views.new_user,name="New_user page"),
    path('user',views.user,name='user'),
    path('home2',views.home2,name="home2"),
    path('update_data',views.update,name="updtaing"),
    path('vc',views.vc,name="data"),
    path('display_data',views.display_data,name="show"),
    path('delete_now',views.delete_dt,name="delete"),
    path('login_here',views.Login_here,name="login"),
    path('downloadpage',views.downloadpage,name="download"),
    path('dwn_file',views.dwn_file,name="down_file"),
    path('sendmail',views.sendmail,name="email"),
    #path('branch',views.branch,name="selection"),
    path('table3',views.table,name="table"),
    path('table2',views.dis_record,name="table2"),
    path('dwn2_file',views.down2_file,name='assignment download'),
    path('dwn3_file',views.down3_file,name="result")

]

