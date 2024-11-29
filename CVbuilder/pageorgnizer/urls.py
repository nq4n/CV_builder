from django.urls import path 
from . import views
#import httpsrequests


urlpatterns = [
    path("" ,views.home,name="home"),
    path ("home.html",views.home,name="home"),
    path("profile",views.profile, name="profile"),
    path("profile.html",views.profile, name="profile"),
    path("output.html" , views.cv_viwer, name="output"),
    path("view", views.cv_viwer, name="output"),
    path("CV_builder.html",views.cv_made, name="CV_builder"),
    path("save_cv",views.save_cv, name="save"),
]
# make list of paths that are gettning infromation from html page 
