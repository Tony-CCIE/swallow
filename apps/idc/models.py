from django.db import models
from server.models import Server


# Create your models here.
class Idc(models.Model):
    """
    Idc模型
    """
    idc_name = models.CharField("机房名称", max_length=32, unique=True, help_text="机房名称")
    address = models.CharField("机房地址", null=True, max_length=128, help_text="机房地址")
    phone = models.CharField("机房电话", null=True, max_length=16, help_text="机房电话")
    remark = models.TextField("备注", null=True, max_length=255, help_text="备注")
    create_date = models.DateTimeField("创建时间", blank=True, null=True, auto_now_add=True, max_length=32,
                                       help_text="创建时间")
    update_date = models.DateTimeField("更新时间", blank=True, null=True, auto_now=True, max_length=32, help_text="更新时间")

    class Meta:
        verbose_name = 'IDC机房'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.idc_name


class Cabinet(models.Model):
    """
    机柜模型
    """
    cabinet_name = models.CharField("机柜号", max_length=10)
    idc = models.ForeignKey(Idc, verbose_name="所处机房", on_delete=models.CASCADE, related_name='cabinet')

    class Meta:
        verbose_name = '机柜'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.cabinet_name


class Uposition(models.Model):
    """
    机柜U位模型
    """
    u_name = models.CharField("U位", help_text="U位", max_length=2)
    cabinet = models.ForeignKey(Cabinet, verbose_name="所处机柜", on_delete=models.CASCADE, null=True, blank=True,
                                related_name='uposition')
    server = models.ForeignKey(Server, verbose_name="服务器", on_delete=models.CASCADE, null=True, blank=True,
                                related_name='u_server')

    class Meta:
        verbose_name = '机柜U位'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.u_name
