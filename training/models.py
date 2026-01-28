from django.db import models
from accounts.models import CustomUser

# Create your models here.

#class MenuPost(models.Model):
#    user = models.ForeignKey(CustomUser, verbose_name='ユーザ', on_delete=models.CASCADE)
#    title = models.CharField(verbose_name='タイトル', max_length=200)
#       # 投稿日時のフィールド
#    posted_at = models.DateTimeField(verbose_name='投稿日時',auto_now_add=True)
#    def __str__(self):
#        return self.title
#    class Meta:
#        verbose_name = 'メニューポスト'
#        verbose_name_plural = 'メニューポスト一覧'
#        ordering = ['-posted_at']

class MenuItem(models.Model):
    
    #post = models.ForeignKey(MenuPost, related_name='items', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザ', on_delete=models.CASCADE,)
    parts = models.CharField(verbose_name='部位', max_length=20,)
    content = models.CharField(verbose_name='種目', max_length=100,)
    weight = models.CharField(verbose_name='重量', max_length=10,)
    rep = models.CharField(verbose_name='回数', max_length=10,)
    memo = models.TextField(verbose_name='メモ',null=True,)
           # 投稿日時のフィールド
    posted_at = models.DateField(verbose_name='投稿日時',auto_now_add=True,)

    def __str__(self):
        return self.parts

    
#    class Meta:
#        verbose_name = 'メニューポスト'
#        verbose_name_plural = 'メニューポスト一覧'
#        ordering = ['-posted_at']

class Record(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    weight = models.IntegerField(default=0,blank=True)
    rep = models.IntegerField(default=0,blank=True)
    memo = models.TextField(blank=True)

    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.menu_item.content}"
        
