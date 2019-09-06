from django.db import models

# Create your models here.


class Paragraph(models.Model):
    text = models.TextField(max_length=20000,null=False,blank=False)

    def __str__(self):
        return self.text