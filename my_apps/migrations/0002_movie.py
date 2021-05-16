# Generated by Django 3.2.2 on 2021-05-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('mv_original', models.FileField(blank=True, null=True, upload_to='media/movies/')),
                ('mv_480', models.FileField(blank=True, null=True, upload_to='media/movies/')),
                ('mv_720', models.FileField(blank=True, null=True, upload_to='media/movies/')),
                ('audio', models.FileField(blank=True, null=True, upload_to='media/movies/')),
            ],
        ),
    ]