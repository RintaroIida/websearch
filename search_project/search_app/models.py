from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255) #名前
    description = models.TextField() #説明
    price = models.DecimalField(max_digits=10, decimal_places=2) #値段
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # 1はカテゴリID
    horsepower = models.IntegerField(default=0)  # 馬力（小数点なし）
    seatheight = models.IntegerField(default=0)  # シート高（小数点なし）
    cylindercount = models.IntegerField(default=0)# シリンダー数
    displacement = models.IntegerField(default=0)  # 排気量（小数点なし）
    maximumtorque = models.IntegerField(default=0)  # 最大トルク（小数点なし）
    weight = models.IntegerField(default=0)  # 重量（小数点なし）    
    image_url = models.URLField(null=True, blank=True)  # 画像のURLフィールド
    bike_type = models.ForeignKey('BikeType', on_delete=models.SET_NULL, null=True, blank=True)  # 新しい外部キー
    def __str__(self):
        return self.name
    

class BikeType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
