# Generated by Django 4.2.6 on 2023-11-30 15:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decky', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Kategori'},
        ),
        migrations.AddField(
            model_name='kategori',
            name='banner_satu',
            field=models.ImageField(null=True, upload_to='gambar/banner'),
        ),
        migrations.AddField(
            model_name='produk',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]