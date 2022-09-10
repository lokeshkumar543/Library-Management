from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from Myapp import views
urlpatterns = [
   path('',views.signup,name='signup'),
   path('login/',views.user_login,name='login'),
   path('logout/',views.user_logout,name='logout'),
   path('home/',views.home,name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)