from django.db import models

# Create your models here.
class Content(models.Model):
    cId = models.AutoField(primary_key=True)
    content = models.CharField(max_length=20)
    creatTime = models.DateTimeField(auto_now_add=True)#保存创建的时间
    updateTime = models.DateTimeField(auto_now=True)#保存每次修改的时间

    class Meta:
        db_table='Content'