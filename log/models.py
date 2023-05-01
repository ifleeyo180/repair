from django.db import models
from django.core.exceptions import ValidationError


def validate_image_size(image):
    file_size = image.file.size
    limit_mb = 1
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)
# Tag


class Tag(models.Model):
    subject = models.CharField(max_length=10)
    Rstyle = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.subject


class LogItem(models.Model):
    # 處理進度的選項清單
    ST_OPTIONS = [
        (0, '待處理'),
        (1, '處理中'),
        (2, '已結案'),
    ]
    # 報修主旨
    subject = models.CharField('報修主旨', max_length=255)
    # 報修內容
    description = models.TextField('報修內容')
    # 報修人
    reporter = models.CharField('報修人', max_length=30)
    # 聯絡電話
    phone = models.CharField('聯絡電話', max_length=30)
    # 報修時間
    ctime = models.DateTimeField('報修時間', auto_now_add=True)
    # --------------------------------------------------
    # 處理人員
    handler = models.CharField('處理人員', max_length=30)
    # 處理進度
    status = models.IntegerField(
        '處理進度',
        default=0,
        choices=ST_OPTIONS
    )
    # 處理說明
    comment = models.TextField('處理說明')
    # 最後更新時間
    utime = models.DateTimeField('最後更新時間', auto_now=True)
    # 照片
    picture = models.ImageField(
        '照片', blank=True, null=True, validators=[validate_image_size])
    # Tag
    tags = models.ManyToManyField(
        Tag, through='Tagmanagement', through_fields=('logitem', 'tag'))

    def __str__(self):
        return self.subject
    # 根據 status 的值傳回對應的 class 字串,
    # 0 傳回 'danger', 1 傳回 'warning', 2 傳回 'success'

    def get_status_class(self):
        return ['danger', 'warning', 'success'][self.status]


class TagManagement(models.Model):
    logitem = models.ForeignKey(LogItem, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
