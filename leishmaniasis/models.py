import uuid

from django.db import models

class Leishmaniasis(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)    
    img = models.ImageField(upload_to='img/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.img.name