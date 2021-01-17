  
from django.contrib import admin
from mptt import admin as mptt_admin
from course import models

class LessonAdmin(mptt_admin.DraggableMPTTAdmin):
    pass

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal=('lessons', )


admin.site.register(models.Lesson, LessonAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Level)