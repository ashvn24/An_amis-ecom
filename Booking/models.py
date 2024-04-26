from django.db import models
from users.models import CustomUser
# Create your models here.


available = (
    ('9:30-10:30','9:30-10:30'),
    ('10:30-11:30','10:30-11:30'),
    ('11:30-12:30','11:30-12:30'),
    ('12:30-1:30','12:30-1:30'),
    ('1:30-2:30','1:30-2:30'),
    ('2:30-3:30','2:30-3:30'),
    ('3:30-4:30','3:30-4:30'),
    ('4:30-5:30','4:30-5:30'),
    ('5:30-6:30','5:30-6:30'),
    ('6:30-7:30','6:30-7:30'),
)

class Book(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    time = models.CharField(choices=available)
    date = models.DateField()
    
    def __str__(self):
        return self.user.email