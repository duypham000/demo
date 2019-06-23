from django.db import models

# Create your models here.
class Posts(models.Model):
    # kiểu ký tự với maxlenght là 100
    title = models.CharField(max_length=100)
    body = models.TextField()
    # kiểu ngày giờ với tự động thêm ngày giờ hiện tại
    date = models.DateTimeField(auto_now_add=True)
