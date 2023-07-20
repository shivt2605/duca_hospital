from email.mime import image
from email.policy import default
from unicodedata import name
from django.db import models

from django.utils.text import slugify
from django.db.models.signals import pre_save

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
## logo
class Companylogo(models.Model):
    image = models.ImageField(upload_to='slider/img')
    name = models.CharField(max_length=250,null=True)    
    def __str__(self):
        return self.name

# Events 

EVENTS = (
        ('UPCOMING','UPCOMING'),
        ('COMPLETATE','COMPLETATE'),        

    )

class Event(models.Model):
    image = models.ImageField(upload_to='slider/img')
    name = models.CharField(max_length=250,null=True)
    event = models.CharField(choices=EVENTS,max_length=20)
    description = models.CharField(max_length=500,null=True)       
    date = models.DateTimeField(blank=True, null=True)      
    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=250,null=True)
    answers = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.question




#1 Slider
class Slider(models.Model):
    image = models.ImageField(upload_to='slider/img')
    line_1 = models.CharField(max_length=250,null=True)
    line_2 = models.CharField(max_length=250,null=True)
    line_3 = models.CharField(max_length=250,null=True)
    line_4 = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.line_1

COLOR = (
        ('primary','primary'),
        ('secondary','secondary'),       
        ('success','success'),       
        ('danger','danger'),       
        ('warning','warning'),       
        ('info','info'),       
        ('dark','dark'),       
        ('body','body'),     
        ('white','white'),     
        ('transparent','transparent'),     
        ('light','light'),     
    )
#1 Slider
class Header(models.Model):
    logo = models.ImageField(upload_to='slider/img')
    color = models.CharField(choices=COLOR,max_length=100)
    number = models.CharField(max_length=12,null=True)
    contant_1 = models.CharField(max_length=250,null=True)
    contant_2 = models.CharField(max_length=250,null=True)
    contant_3 = models.CharField(max_length=250,null=True)
    
    def __str__(self):
        return self.number
    
class Footer(models.Model):
    color = models.CharField(choices=COLOR,max_length=100)
    facebook  = models.CharField(max_length=250,null=True)
    youtube = models.CharField(max_length=250,null=True)
    whatsApp = models.CharField(max_length=250,null=True)
    instagram = models.CharField(max_length=250,null=True)
    telegram = models.CharField(max_length=250,null=True)
    pinterest = models.CharField(max_length=250,null=True)
    twitter = models.CharField(max_length=250,null=True)
    linkedIn = models.CharField(max_length=250,null=True)
    copyright = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.facebook




class Back_Graound(models.Model):
    name = models.CharField(max_length=500,null=True)
    fqa = models.ImageField(upload_to='BackGraound')
    blog = models.ImageField(upload_to='BackGraound')
    blog_details = models.ImageField(upload_to='BackGraound')
    wishlist = models.ImageField(upload_to='BackGraound')
    doctor = models.ImageField(upload_to='BackGraound')
    doctor_details = models.ImageField(upload_to='BackGraound')
    service = models.ImageField(upload_to='BackGraound')
    service_details = models.ImageField(upload_to='BackGraound')
    media = models.ImageField(upload_to='BackGraound')

    contact = models.ImageField(upload_to='BackGraound')
    def __str__(self):
        return self.name

#1 Slider
class Content_Slider(models.Model):
    contant_1 = models.CharField(max_length=250,null=True)
    contant_2 = models.CharField(max_length=250,null=True)
    contant_3 = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.contant_1


#1 Slider
class Meta(models.Model):
    favicon = models.ImageField(upload_to='favicon')
    title = models.CharField(max_length=500,null=True)
    keyword = models.CharField(max_length=500,null=True)
    discriptaion = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.title




# 2 Banner
class Banner(models.Model):
    image = models.ImageField(upload_to='banner/img')
    name = models.CharField(max_length=250,null=True)
    line_1 = models.CharField(max_length=250,null=True)
    line_2 = models.CharField(max_length=250,null=True)   
    def __str__(self):
        return self.name



GENDER = (
        ('Male','Male'),
        ('Female','Female'),       
    )

#0 category
class DepartMent(models.Model):
    image = models.ImageField(upload_to='slider/img')
    name = models.CharField(max_length=250,null=True)
    name_hindi = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=250,null=True)
    
    def __str__(self):
        return self.name


#5 Depatment
class Service(models.Model):   
    department = models.ForeignKey(DepartMent,on_delete=models.CASCADE)	
    service_name = models.CharField(max_length=250,null=True)
    hindi_name = models.CharField(max_length=250,null=True)
    sort_description = models.CharField(max_length=250,null=True)
    future_image = models.ImageField(upload_to='service/img')   
    description = RichTextField()
    slug = models.SlugField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.service_name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("service_details",kwargs={'slug':self.slug})

    class Meta:
        db_table = "app_Service"
    

def create_slug(instance, new_slug=None):
    slug = slugify(instance.service_name)
    if new_slug is not None:
        slug = new_slug
    qs = Service.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_reciver, Service)


#8 Media
class Media(models.Model):
    image = models.ImageField(upload_to='service/media')
    title = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.title

#9 TPA
class Tpa(models.Model):
    image = models.ImageField(upload_to='service/tpa')
    company = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.company

#10 Featured
class Featured(models.Model):
    image = models.ImageField(upload_to='service/featured')
    name = models.CharField(max_length=250,null=True)
    title = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.name

#10 Social
class Social(models.Model):
    icon = models.ImageField(upload_to='service/social')
    name = models.CharField(max_length=250,null=True)
    link = models.CharField(max_length=550,null=True)
    def __str__(self):
        return self.name

#11 Team
class Team(models.Model):
    image = models.ImageField(upload_to='service/team')
    name = models.CharField(max_length=250,null=True)
    title = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.name

class Contact(models.Model):    
    where_we_are=models.CharField(max_length=2000)
    form_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    number=models.CharField(max_length=255)
    email_id=models.EmailField(max_length=255)
    location_map = models.CharField(max_length=2500,null=True, blank=True)
    def __str__(self):
        return self.where_we_are
    
class About(models.Model):   
    image = models.ImageField(upload_to='slider/img') 
    main_title=models.CharField(max_length=2000)
    experience=models.CharField(max_length=3)
    title=models.CharField(max_length=255)
    sub_title=models.CharField(max_length=255)    
    how_to_work=models.CharField(max_length=255)
    mission =models.CharField(max_length=2000)
    vision =models.CharField(max_length=2000)
    values =models.CharField(max_length=2000)
    def __str__(self):
        return self.main_title
    

    