from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)    #포스트 제목
    content = models.TextField()        #내용
    pub_date = models.DateTimeField()   #작성일
    modify_date = models.DateTimeField(null=True, blank=True)   #수정일
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                              null=True, blank=True)

    def __str__(self):
        return self.title