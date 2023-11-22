from django.db import models

class Mi_API_rest(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=300)

    def __str__(self):
        return self.name