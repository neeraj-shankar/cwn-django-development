from django.contrib import admin
from PortfolioApp.models import About,Contact, Service, Skill

# Register your models here.
admin.site.register(About)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     # To display the fields to add post in post list
    fields = ('name', 'email', 'subject', 'desc')

    # Show the multiple columns on admin page of PostList
    list_display = ('name', 'email', 'subject' )

    #add search field option for post lists
    search_fields = ('name', 'email')

    # list_filter - adding filter option
    list_filter = ('name', 'email')

    # ordernig 
    ordering =('name', 'email')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
     # To display the fields to add post in post list
    fields = ('title', 'desc')

    # Show the multiple columns on admin page of PostList
    list_display = ('title', )

    #add search field option for post lists
    search_fields = ('title', )

    # list_filter - adding filter option
    list_filter = ('title', )

    # ordernig 
    ordering =('title', )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
     # To display the fields to add post in post list
    fields = ('type', 'desc')

    # Show the multiple columns on admin page of PostList
    list_display = ('type', )

    #add search field option for post lists
    search_fields = ('type',)

    # list_filter - adding filter option
    list_filter = ('type',)

    # ordernig 
    ordering =('type',)
