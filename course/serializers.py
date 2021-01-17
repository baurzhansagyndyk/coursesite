from rest_framework import serializers
from course import models

class LevelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Level
        fields = ('id', 'level_value', 'level_description', 'model')

        