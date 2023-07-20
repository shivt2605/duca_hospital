from multiprocessing import context
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from app.models import *
from pharmacy.models import *
from blog.models import *
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.


def home(request):

    sliders = Slider.objects.all()
    banners = Banner.objects.all().order_by('-id')[0:3]
    banners_2 = Banner.objects.all().order_by('-id')[3:5]
      
    meida_galler = Media.objects.filter().order_by('-id')[0:10]
    doctors = Doctor.objects.all().order_by('-id')[0:2]
    department = DepartMent.objects.all()
    service = Service.objects.all()[0:4]
    tpas = Tpa.objects.all()
    upcoming = Event.objects.filter(event = 'UPCOMING').order_by('-id')[0:5]
    completate = Event.objects.filter(event = 'COMPLETATE').order_by('-id')[0:4]
    social_media = Social.objects.all()
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    content_clider= Content_Slider.objects.all().order_by('-id')[0:1]
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    context = {
        'sliders': sliders,
        'banners': banners,
        'banners_2': banners_2,
        'department': department,        
        'tpas': tpas,
        'meida_galler': meida_galler,
        'doctors': doctors,
        'social_media': social_media,
        'upcoming': upcoming,
        'completate': completate,
        'header': header,
        'footer': footer,
        'meta': meta,
        'service': service,
        'content_clider': content_clider,
        'bg': bg,
    }
    return render(request, 'home.html', context)

def about(request):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    about= About.objects.all().order_by('-id')[0:1]
    our_team= Team.objects.all().order_by('-id')
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()
    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'about': about,
        'our_team': our_team,
        'bg': bg,
        'department': department,
    }
    return render(request, 'about.html',context)

def contact(request): 
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    content_clider= Content_Slider.objects.all().order_by('-id')[0:1]
    contact= Contact.objects.all().order_by('-id')[0:1]
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()


    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'content_clider': content_clider,
        'contact': contact,
        'bg': bg,
        'department': department,

    }       
    return render(request, 'contact.html',context )


def faq(request):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    fqa= Faq.objects.all().order_by('-id')[0:1]
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()
    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'fqa': fqa,
        'bg': bg,
        'department': department,
    }
    
    return render(request, 'faq.html',context )



def service(request):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    service = Service.objects.all()
    department = DepartMent.objects.all()
    bg = Back_Graound.objects.all().order_by('-id')[0:1]

    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'service': service,
        'bg': bg,
        'department': department,
    }
        
    return render(request, 'service.html', context)

def service_details(request,slug):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1] 
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()

    service = Service.objects.filter(slug = slug)
    if service.exists():
        service = Service.objects.get(slug = slug)
    else:
        return redirect('404')    
    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'service': service,
        'bg': bg,
        'department': department,
    }   
    return render(request, 'service_details.html',context )

def filter_data(request):
    department = request.GET.getlist('department[]')
   

    allService = Service.objects.all().order_by('-id').distinct()
    if len(department) > 0:
        allService = allService.filter(department__id__in=department).distinct()

    
    t = render_to_string('ajax/service.html', {'service': allService})

    return JsonResponse({'data': t})



def doctor(request): 
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()



    
    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'department': department,
        'bg': bg,

    }
       
    return render(request, 'doctor.html',context)

def doctor_details(request,slug): 
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()

    
    doctor = Doctor.objects.filter(slug = slug)
    if doctor.exists():
        doctor = Doctor.objects.get(slug = slug)
    else:
        return redirect('404')  
   
    context = {
        'header': header,
        'footer': footer,
        'meta': meta,        
        'doctor': doctor,        
        'bg': bg,        
        'department': department,        
    }       
    return render(request, 'doctor_view.html',context)



def wishlist(request):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()


    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'bg': bg,
        'department': department,
    }        
    return render(request, 'wishlist.html',context)


def blog(request):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    Popular = Post.objects.filter(Popular = 'True',status=1).order_by('-id')    
    Recent = Post.objects.filter(Recent = 'True',status=1).order_by('-id')[0:4]
    main_post = Post.objects.filter(main_post = 'True',status=1)[0:1]
    Editors_Pick = Post.objects.filter(section = 'Editors_Pick',status=1).order_by('-id')
    Trending = Post.objects.filter(section = 'Trending',status=1).order_by('-id')
    Inspiration = Post.objects.filter(section = 'Inspiration',status=1).order_by('-id')
    Latest_Post = Post.objects.filter(section = 'Latest_Post',status=1).order_by('-id')
    blogcategory = Blog_Category.objects.all()
    tag = Tag.objects.all()    
    post = Post.objects.filter(status=1).order_by('-id')
    paginator = Paginator(post,1)
    page_number =request.GET.get('page')
    postfinel=paginator.get_page(page_number)
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()
    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'tag': tag,    
        'Popular':Popular,
        'post':post,
        'Recent':Recent,
        'main_post':main_post,
        'Editors_Pick':Editors_Pick,
        'Trending':Trending,
        'Inspiration':Inspiration,
        'Latest_Post':Latest_Post,
        'blogcategory':blogcategory,
        'postfinel':postfinel,
        'bg':bg,
        'department':department,
    } 
    return render(request, 'blog.html',context)


def blog_details(request,slug):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    Popular = Post.objects.filter(Popular = 'True',status=1).order_by('-id')
    blogcategory = Blog_Category.objects.all()
    tag = Tag.objects.all()
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()

    post = Post.objects.filter(slug = slug)
    
    if post.exists():
        post = Post.objects.get(slug = slug)
    else:
        return redirect('404')

    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'post': post,
        'Popular': Popular,
        'blogcategory': blogcategory,
        'tag': tag,
        'bg': bg,
        'department': department,

    }        
    return render(request, 'blog-details.html',context)


def MEDIA(request):
    header = Header.objects.all().order_by('-id')[0:1]
    footer = Footer.objects.all().order_by('-id')[0:1]
    meta = Meta.objects.all().order_by('-id')[0:1]
    media = Media.objects.all()
    bg = Back_Graound.objects.all().order_by('-id')[0:1]
    department = DepartMent.objects.all()


    context = {
        'header': header,
        'footer': footer,
        'meta': meta,
        'media': media,
        'bg': bg,
        'department': department,
    }
        
    return render(request, 'media.html', context)
