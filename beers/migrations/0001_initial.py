# Generated by Django 2.1.5 on 2019-01-06 22:11

import beers.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('abv', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Alcohol by volumen')),
                ('is_filtered', models.BooleanField(default=False, verbose_name='Is filtered?')),
                ('color', models.SmallIntegerField(choices=[(1, 'amarillo'), (2, 'negro'), (3, 'ámbar'), (4, 'marron')], default=1, verbose_name='Color')),
                ('image', models.ImageField(blank=True, null=True, upload_to=beers.utils.image_upload_location, verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Beer',
                'verbose_name_plural': 'Beers',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete='Created by', related_name='beers_company_created', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_company_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='SpecialIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('beers', models.ManyToManyField(blank=True, related_name='special_ingredients', to='beers.Beer')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete='Created by', related_name='beers_specialingredient_created', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_specialingredient_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'verbose_name': 'Special ingredient',
                'verbose_name_plural': 'Special ingredients',
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='beer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beers', to='beers.Company'),
        ),
        migrations.AddField(
            model_name='beer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete='Created by', related_name='beers_beer_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='beer',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_beer_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
    ]
