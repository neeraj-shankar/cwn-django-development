from django.shortcuts import redirect, render
from BlogApp.models import Post
from PortfolioApp.models import About,Contact, Skill, Service
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def HomeView(request):

    #recent_post = PostList.objects.all()
    #setting up pagination
    p = Paginator(Post.objects.all(), 3)
    page = request.GET.get('page')
    recent_post = p.get_page(page)
    
    about_me = About.objects.all()
    my_skill = Skill.objects.all()
    post_list = Post.objects.all()
    my_service = Service.objects.all()
    context = {'recent_post':recent_post, 'about_me':about_me,'post_list':post_list, 
                'my_skill':my_skill,'my_service' :my_service, 'nbar': 'home' }

    return render(request, 'portfolio/portfolio.html', context)

def ContactView(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject= request.POST.get('subject')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, subject=subject, desc=desc)
        contact.save()
        messages.success(request, 'Thank you for your message. We will get back to you soon')
        return redirect ('home_page')
    return render(request, 'portfolio/contact.html')
    