from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.utils import timezone
from django.db.models import ImageField

import os
import uuid


# Create your models here.



class Nuc(models.Model):
    name = models.CharField('이름', max_length=10)
    ip = models.GenericIPAddressField('ip주소')
    place = models.CharField('위치', max_length=100)


    def __str__(self):
        return self.name


def person_directory_path(instance, filename):
    return 'person_{0}/{1}'.format(instance.id, filename)

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('이름', max_length=10)
    missing_place = models.CharField('실종 지역', max_length=10)
    missing_date = models.DateTimeField('실종 일시')
    age = models.PositiveSmallIntegerField('나이')
    character = models.CharField('특징', max_length=500)
    image = models.ImageField('사진', upload_to=person_directory_path)
    registered_nuc = models.ForeignKey('Nuc', models.PROTECT, verbose_name='등록된 눅', related_name='registered_people')
    detected_nuc = models.ManyToManyField('Nuc', verbose_name='발견된 눅', through='DetectedInformation')
    is_found = models.BooleanField()

    def __str__(self):
        return self.name

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))
    
def detected_person_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'person_{0}/{1}-{2}-{3}'.format(
        instance.person.id,
        timezone.localtime().strftime('%Y%m%d-%H:%M:%S'),
        instance.detected_nuc.name,
        filename
    )

class DetectedInformation(models.Model):
    person = models.ForeignKey(Person, models.CASCADE, verbose_name='실종자')
    image = models.ImageField('사진', upload_to=detected_person_directory_path)
    detected_nuc = models.ForeignKey('Nuc', models.PROTECT, verbose_name='발견한 눅')
    time = models.DateTimeField('발견 시간', auto_now=True)
    match_rate = models.DecimalField('일치율', max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['match_rate']

    def __str__(self):
        return '{0} was found at {1}'.format(self.person, self.detected_nuc)

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))
