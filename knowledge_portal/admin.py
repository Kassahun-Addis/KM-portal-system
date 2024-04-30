from django.contrib import admin
from .models import Contact, Message, Question, Response, Room,BlogPost, UploadedFile, MessageUser, MyModel

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(BlogPost)
admin.site.register(UploadedFile)
admin.site.register(MessageUser)
admin.site.register(MyModel)

