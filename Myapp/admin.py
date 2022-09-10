from pyexpat import model
from django.contrib import admin
from .models import StudentUser,User,Book
# Register your models here.
@admin.register(StudentUser)
class StudentAdmin(admin.ModelAdmin):
    list_display=['full_name','username']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['fullname','email']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['book_title','book_subject','book_price','book_images']