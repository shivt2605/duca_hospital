from django.contrib import admin
from .models import *

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','future_image','department','service_name',)


class FaqAdmin(admin.ModelAdmin):    
    list_display = ('id','question','answers')
    list_editable = ('question','answers')


class AboutAdmin(admin.ModelAdmin):    
    list_display = ('id','main_title','experience','title','sub_title','how_to_work','mission','vision','values')


class HeaderAdmin(admin.ModelAdmin):    
    list_display = ('id','color','number','contant_1','contant_2','contant_3')

class FooterAdmin(admin.ModelAdmin):    
    list_display = ('id','color','facebook','youtube','whatsApp','instagram','telegram','pinterest','twitter','linkedIn','copyright')

class MetaAdmin(admin.ModelAdmin):    
    list_display = ('id','title','keyword','discriptaion',)

class ContactAdmin(admin.ModelAdmin):    
    list_display = ('id','where_we_are','form_name','address','number','email_id','location_map')

class EventAdmin(admin.ModelAdmin):    
    list_display = ('id','name','event','description')

class SliderAdmin(admin.ModelAdmin):    
    list_display = ('id','line_1','line_2','line_3')

class TeamAdmin(admin.ModelAdmin):  
    list_display = ('id','image','name','title','description',)

class Back_GraoundAdmin(admin.ModelAdmin):  
    list_display = ('id','name','fqa','blog','blog_details',)


admin.site.register(Header,HeaderAdmin)
admin.site.register(Footer,FooterAdmin)
admin.site.register(Meta,MetaAdmin)
admin.site.register(Content_Slider)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Faq,FaqAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Companylogo)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(Banner)
admin.site.register(DepartMent)
admin.site.register(About,AboutAdmin)

admin.site.register(Media)
admin.site.register(Tpa)
admin.site.register(Featured)
admin.site.register(Social)
admin.site.register(Back_Graound,Back_GraoundAdmin)


admin.site.register(Team,TeamAdmin)







