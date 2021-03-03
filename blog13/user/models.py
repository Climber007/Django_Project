from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    class Meta:  # 定义meta类；
        db_table = 'user'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, null=False)
    email = models.CharField(max_length=64, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)

    def __repr__(self):
        return '<User {} {}>'.format(self.id, self.name)

    __str__ = __repr__