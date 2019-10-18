# Generated by Django 2.2.6 on 2019-10-18 11:36

from django.db import migrations, models
import marketing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=marketing.models.slider_upload)),
                ('slider_order', models.IntegerField(default=0)),
                ('header_text', models.CharField(blank=True, max_length=150, null=True)),
                ('text', models.CharField(blank=True, max_length=150, null=True)),
                ('active', models.BooleanField(default=False)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('start_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
