# Generated by Django 4.1.7 on 2023-05-03 12:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog-images')),
                ('body2', models.TextField(blank=True, null=True)),
                ('image2', models.ImageField(blank=True, null=True, upload_to='blog-images')),
                ('body3', models.TextField(blank=True, null=True)),
                ('image3', models.ImageField(blank=True, null=True, upload_to='blog-images')),
                ('video', models.FileField(blank=True, null=True, upload_to='blog-videos')),
                ('meta_description', models.CharField(blank=True, max_length=150)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tag')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
