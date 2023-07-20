from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
   

    path('blog', views.blog, name='blog'),
    path('blog_details/<slug:slug>', views.blog_details, name='blog_details'),
    
    
    
    path('contact', views.contact, name='contact'),
    path('media', views.MEDIA, name='media'),
    path('faq', views.faq, name='faq'),
    
    path('service', views.service, name='service'),
    path('service/filter-data',views.filter_data,name='filter-data'),

    path('service_details/<slug:slug>', views.service_details, name='service_details'),
    

    path('doctor_details/<slug:slug>', views.doctor_details, name='doctor_details'),
    path('doctor', views.doctor, name='doctor'),
    path('wishlist', views.wishlist, name='wishlist'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)