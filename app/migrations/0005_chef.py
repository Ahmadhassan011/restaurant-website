# Generated by Django 5.0.7 on 2024-08-10 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_desssert_main_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='website/static/Chefs/')),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
