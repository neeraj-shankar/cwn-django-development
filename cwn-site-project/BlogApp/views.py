from django.core.checks import messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from BlogApp.models import Category, Author, Post,  Comment
from BlogApp.forms import CategoryForm,PostForm

# Create your views here.
def CategoryView(request):
    category_list = Category.objects.all()
    post_list = Post.objects.all()
    return render(request, 'blogs/category.html', {'category_list':category_list, 'post_list':post_list})



#************************ View for adding category using form*******************
def AddCategoryView(request):
    submitted = False
    if request.method == "POST":
        cat_form = CategoryForm(request.POST, request.FILES)
        if cat_form.is_valid():
            cat_form.save()
            return redirect('home_page')
    
    else:
        cat_form = CategoryForm
        if 'submitted' in request.GET:
            submitted = True

   
    return render(request, 'blogs/add-category.html', {'cat_form':cat_form, 'submitted': submitted})

#************************ View for updating the post category using form*******************
def EditCategoryView(request, cat_id):
    cat_detail = Category.objects.get(slug=cat_id)
    edit_category = CategoryForm(request.POST or None, instance=cat_detail)
    if edit_category.is_valid():
        edit_category.save()
        return redirect('category_page')

    return render(request, 'blogs/edit-category.html', {'edit_category':edit_category})

#************************ View for updating the post category using form*******************


#************************ View for Post Lists*******************
def PostListView(request):
    post_list = Post.objects.all()
    return render(request, 'blogs/posts.html', {"post_list":post_list})

#************************ View for adding post using form*******************
def AddPostView(request):
    
    submitted = False
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('category_page')
    
    else:
        post_form = PostForm
        if 'submitted' in request.GET:
            submitted = True

   
    return render(request, 'blogs/add-post.html', {'post_form':post_form, 'submitted': submitted})

#************************ View for updating the post using form*******************
def EditPostView(request, post_id):
    post_detail = Post.objects.get(sno_post=post_id)
    edit_post = PostForm(request.POST or None, instance=post_detail)
    if edit_post.is_valid():
        edit_post.save()
        return redirect('category_page')

    return render(request, 'blogs/edit-post.html', {'edit_post':edit_post})

#**************************View for post details*****************
def PostDetailView(request, post_id):
    post_detail = Post.objects.get(sno_post=post_id)
    post_comment = Comment.objects.filter(post=post_detail)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("comment")
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno_post=post_id)
        comment = Comment(name=name, email=email, desc=desc, post=post)
        comment.save()
        redirect (f"article/{post_detail.sno_post}" )
        
       
    post_sidebar = Post.objects.all()
    post_category = Category.objects.all()
    context = {'post_detail':post_detail,'post_sidebar':post_sidebar,'post_category':post_category, 'post_comment':post_comment}
    
    return render(request, 'blogs/post-detail.html',context )


#********************************View for sidebar**************************
#def blog_sidebar_page(request):
    #sidebar_detail= PostList.objects.all()
    #return render(request, 'sidebar.html')

def CategorizedListView(request, cats):
    categorized_post_list = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'blogs/categorized-posts.html', {'cats':cats, 'categorized_post_list':categorized_post_list})

