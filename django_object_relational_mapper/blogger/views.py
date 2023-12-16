from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post
from utility.logger import setup_logger
from django.db import transaction

log = setup_logger(__name__)

# Create your views here.


def home_page(request):
    return render(request, "base.html")


def show_author_list(request):
    if request.method == "POST":
        # Get form data from the POST request
        name = request.POST.get("author")
        email = request.POST.get("email")
        origin = request.POST.get("origin")
        bio = request.POST.get("description")

        # Storing in the dictionary just for logging
        received_data = {"name": name, "email": email, "origin": origin, "bio": bio}
        log.info(f"Author Data Received --> {received_data}")

        # Use an atomic transaction to create the blog post and related objects
        with transaction.atomic():
            try:
                author_detail = Author.objects.create(
                    name=name, email=email, origin=origin, bio=bio
                )

            except Exception as ex:
                # Handle any exceptions that may occur during the transaction
                # Rollback the transaction if an exception occurs
                transaction.set_rollback(True)
                log.error(
                    f" Error occurred during handling the transaction--> {str(ex)}"
                )

        transaction.commit()

    authors = Author.objects.all()
    context = {"author_list": authors}
    return render(request, "blogger/index.html", context=context)



def post_management(request):

    if request.method == "POST":
        log.info(f"Yes! The request is correct")
        log.info(request.body)

    posts = Post.objects.all()
    context = {"post_list": posts}

    return render(request, "blogger/post.html", context=context)
