# Generated by Django 4.1 on 2022-11-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_staffs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]