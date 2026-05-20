
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
 
    path('user_home',views.user_home,name='user_home'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('view_userposted_complaints',views.view_userposted_complaints,name='view_userposted_complaints'),
    path('load-subcategories/', views.load_subcategories, name='load_subcategories'),
    path('load-fine/', views.load_fine, name='load_fine'),

    path('RegisterComp/<int:offence_id>/',views.RegisterComp,name='RegisterComp'),
    
    
    path('traffic_home',views.traffic_home,name='traffic_home'),
    path('trf_police_collect_fine',views.trf_police_collect_fine,name='trf_police_collect_fine'),
    
    path("receipt", views.trf_police_collect_fine, name="receipt"),
    path("search_fine_collection", views.search_fine_collection, name="search_fine_collection"),
    path("tiger_vehicle", views.tiger_vehicle, name="tiger_vehicle"),
    
    
    path('track_numberplate',views.track_numberplate,name='track_numberplate'),
    
    
    path("find_my_complaints", views.find_my_complaints, name="find_my_complaints"),
    path("found_vehicle", views.found_vehicle, name="found_vehicle"),
    path("no_parking", views.no_parking, name="no_parking"),
    path('reject_comp/<int:id>',views.reject_comp,name='reject_comp'),
 

    path("fetch_police_details", views.fetch_police_details, name="fetch_police_details"),
    path("fetch_station", views.fetch_station, name="fetch_station"),
    path('logout',views.logout,name='logout'),
    


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
