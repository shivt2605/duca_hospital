from django.contrib import admin

from .models import *
class PostAdmin(admin.ModelAdmin):    
    list_display = ('id','title','hindi_title','category','author','date','status','section','main_post','Popular','Recent',)
    list_editable = ('title','hindi_title','category','author','status','section','main_post','Popular','Recent')



#------------------------------------------------------------------------
admin.site.register(Blog_Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Auther)