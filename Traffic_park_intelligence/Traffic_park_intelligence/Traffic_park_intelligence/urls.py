
from django.contrib import admin
from django.urls import path
from traffic_offence import views


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('userregister',views.userregister,name='userregister'),
    path('rto_home',views.rto_home,name='rto_home'),
    path('rto_view_reg_veh',views.rto_view_reg_veh,name='rto_view_reg_veh'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('admin_addfine',views.admin_addfine,name='admin_addfine'),
    path('admin_createtraffic_pol',views.admin_createtraffic_pol,name='admin_createtraffic_pol'),
    path('delete_police/<int:id>',views.delete_police,name='delete_police'),
    path('delete_tigr/<int:id>',views.delete_tigr,name='delete_tigr'),
 
    



    
    path('logout',views.logout,name='logout'),
    


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
