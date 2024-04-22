from django.contrib import admin
from .models import Room, Message, Contact, Question, Response, BlogPost

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(BlogPost)

