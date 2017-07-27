
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100,verbose_name="식당명",help_text='제목을 입력해 주세요')
    author = models.CharField(max_length=20)
    image = models.ImageField()
    content = models.TextField(max_length=500, verbose_name="내용",null=True, blank=True)
    cdate_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)#('앱이름.tag')

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)#중복 없음
    def __str__(self):
        return self.name
