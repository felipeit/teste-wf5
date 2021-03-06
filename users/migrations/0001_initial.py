# Generated by Django 3.1.7 on 2021-03-10 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ecdtUsuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('idUsuario', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nmUsuario', models.CharField(max_length=80)),
                ('nmEmail', models.CharField(max_length=50, unique=True)),
                ('nmPerfil', models.IntegerField(choices=[(1, 'Junior'), (2, 'Pleno'), (3, 'Sênior')])),
                ('active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
