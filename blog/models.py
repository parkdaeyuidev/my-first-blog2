from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    #메서드 -
    # def는 이거싱 함수/메서드라는 뜻이고, publish는 메서드의 이름이다.
    def publish(self):
        self.published_date = timezone.now()
        self.save()


    #__str__를 호출하면 Post 모델의 제목 string 값을 얻을 수 있다.
    def __str__(self):
        return self.title
