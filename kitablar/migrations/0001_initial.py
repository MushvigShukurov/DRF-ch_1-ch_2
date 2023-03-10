# Generated by Django 4.1.5 on 2023-01-07 12:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=255)),
                ('muellif', models.CharField(max_length=255)),
                ('izah', models.TextField(blank=True, null=True)),
                ('elave_edildi', models.DateTimeField(auto_now_add=True)),
                ('guncellendi', models.DateTimeField(auto_now=True)),
                ('paylasildi', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorum_sahibi', models.CharField(max_length=255)),
                ('yorum', models.TextField(blank=True, null=True)),
                ('elave_edildi', models.DateTimeField(auto_now_add=True)),
                ('guncellendi', models.DateTimeField(auto_now=True)),
                ('paylasildi', models.DateTimeField()),
                ('reytinq', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('kitab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='kitablar.kitab')),
            ],
        ),
    ]
