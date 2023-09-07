# Generated by Django 3.1.14 on 2023-08-16 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('languages', '0003_auto_20230816_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Назва проекту')),
                ('progect_progres', models.PositiveSmallIntegerField(verbose_name='Погрес проекту')),
                ('from_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_language_set', to='languages.program_language', verbose_name='З якої мови')),
                ('to_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_language_set', to='languages.program_language', verbose_name='До якої мови')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекти',
                'ordering': ['from_language'],
            },
        ),
    ]
