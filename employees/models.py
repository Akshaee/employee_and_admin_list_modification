from django.db import models


class Employee(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  email_id = models.EmailField(max_length = 100, unique=True)
  phone_number = models.CharField(max_length = 15, blank = True)
  designation = models.CharField(max_length = 250, default = 'Manager')
  photo = models.ImageField(upload_to = 'images')
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  
  def __str__(self):
    return f"{self.first_name} {self.last_name}"