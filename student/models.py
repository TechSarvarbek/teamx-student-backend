from django.db import models




class Student(models.Model):
    school = models.CharField(max_length=15)
    schoolClass = models.CharField(max_length=5)
    telegramId = models.IntegerField(unique=True)
    image = models.TextField(null=True, blank=True)
    fullname = models.CharField(max_length=20)
    phone = models.IntegerField()
    motto = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    level = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname
