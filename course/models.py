from django.db import models
import time
from mptt import models as mptt_models



def upload_product_img(instance, filename):
    lastDot = filename.rfind('.')
    extension = filename[lastDot:len(filename):1]
    return 'images/product/%s-%s-%s' % (instance.slug, time.time(), extension)


class Lesson(mptt_models.MPTTModel):
    lesson_name = models.CharField(max_length=255)
    parent = mptt_models.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=500, unique=True)

    class MPTTMeta:
        order_insertion_by = ['lesson_name']

    def __str__(self):
        return self.lesson_name

class Level(models.Model):
    level_value = models.CharField(max_length=255)
    level_description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.level_value

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_price = models.IntegerField()
    course_image = models.FileField(upload_to=upload_product_img)
    is_feachered = models.BooleanField(default=False)
    publish_date = models.DateField()
    lessons = mptt_models.TreeManyToManyField(Lesson, related_name='courses')
    slug = models.SlugField(max_length=500)
    level = models.OneToOneField(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name
