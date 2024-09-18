from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField(unique=True, blank=True)
    intro = models.TextField()
    execution_date = models.DateField(default=timezone.now)
    posted_date = models.DateTimeField(auto_now_add=True)
#chatgpt auto slug
    def save(self, *args, **kwargs):
        # まずは一度投稿を保存してposted_dateを設定する
        if not self.id:  # 新しいオブジェクトのときだけ実行
            super().save(*args, **kwargs)
        
        # slugが空の場合、posted_dateを基にslugを生成する
        if not self.slug and self.posted_date:
            self.slug = slugify(self.posted_date.strftime('%Y%m%d-%H%M%S'))
            # slugを設定した後で再度保存
            return super().save(*args, **kwargs)

        super().save(*args, **kwargs)


class Review(models.Model):
    book = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    
    


    