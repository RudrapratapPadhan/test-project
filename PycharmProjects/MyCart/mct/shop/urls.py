from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name="ShopHome"),
   path("about/",views.about,name="AboutUs"),
   path("contact/",views.contact,name="ContactUs"),
   path("tracker/",views.tracker,name="TrackingStatus"),
   path("search/",views.search,name="Search"),
   path("prodview/",views.prodview,name="Search"),
   path("checkout/",views.checkout,name="Checkout"),
   path("login/",views.login,name="Login"),
   #path("/",views.login,name="Login"),

]
