from django.db import models

class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural = 'Yangiliklar tasmasi obunachilari'

    def __str__(self):
        return self.email

    def count_email(self):
        if self.email is not None:
            followers = self.email.count()
        else:
            pass