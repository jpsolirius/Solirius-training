# Generated by Django 4.0.3 on 2022-03-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_id_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(upload_to='projects/static/img/'),
        ),
    ]
