from django.db import models

class Todo_list(models.Model):
    pub_date = models.DateTimeField('date published')
    todo_text =models.CharField(max_length=100)


