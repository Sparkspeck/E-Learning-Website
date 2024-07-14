from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class feedback(models.Model):
    fe_name=models.CharField(max_length=100)
    fe_review=models.CharField(max_length=100)
    fe_condent=models.CharField(max_length=100)
    
    def __str__(self):
        return self.fe_name    

class Meta:
    model=feedback()
 

class Course(models.Model):
    course_title=models.CharField(max_length=50)
    course_amount=models.IntegerField()
    course_img=models.CharField(max_length=20,null=True)
    course_link=models.CharField(max_length=20,null=True)


    def __str__(self):
        return self.course_title
    
class MyCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} "
    
    class Meta:
        unique_together=('user','course')
        