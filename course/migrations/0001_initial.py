# Generated by Django 3.1.3 on 2021-01-16 12:51

import course.models
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_value', models.CharField(max_length=255)),
                ('level_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=500, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='course.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('course_description', models.TextField()),
                ('course_price', models.IntegerField()),
                ('course_image', models.FileField(upload_to=course.models.upload_product_img)),
                ('is_feachered', models.BooleanField(default=False)),
                ('publish_date', models.DateField()),
                ('slug', models.SlugField(max_length=500)),
                ('lessons', mptt.fields.TreeManyToManyField(related_name='courses', to='course.Lesson')),
                ('level', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.level')),
            ],
        ),
    ]
