# Generated by Django 3.1.7 on 2021-03-24 08:05

import content.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField(max_length=300)),
                ('summary', models.CharField(max_length=60)),
                ('document', models.FileField(null=True, upload_to='documents/%Y/%m/%d', validators=[content.validators.validate_file_extension])),
                ('categories', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]