from django.db import models

# Create your models here.
class Blog(models.Model):
  # 어떤 변수에 어떤 타입을 받아줄 지 작성
  title = models.CharField(max_length = 200)
  pub_date = models.DateTimeField('date published')
  body = models.TextField()

  def __str__(self):
    return self.title

  def summary(self):
    return self.body[:100] #100글자 상한선
