from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Kitab(models.Model):
    ad = models.CharField(max_length=255)
    muellif = models.CharField(max_length=255)
    izah = models.TextField(blank=True,null=True)
    elave_edildi = models.DateTimeField(auto_now_add=True)
    guncellendi = models.DateTimeField(auto_now=True)
    paylasildi = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.ad} - {self.muellif}"
class Yorum(models.Model):
    kitab = models.ForeignKey(Kitab,on_delete=models.CASCADE,related_name="yorumlar")
    # yorum_sahibi = models.CharField(max_length=255)
    yorum_sahibi = models.ForeignKey(User, on_delete=models.CASCADE,related_name="kullanici_yorumlari")
    yorum = models.TextField(blank=True,null=True)
    elave_edildi = models.DateTimeField(auto_now_add=True)
    guncellendi = models.DateTimeField(auto_now=True)
    paylasildi = models.DateTimeField()
    reytinq = models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    def __str__(self) -> str:
        return str(self.reytinq)



