# Generated by Django 4.1.1 on 2022-10-07 07:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sportarticle',
            options={'permissions': (('publish_article', 'Can publish article'),)},
        ),
        migrations.AddField(
            model_name='sportarticle',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportarticle',
            name='is_published',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='sportarticle',
            name='published',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='sportarticle',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
