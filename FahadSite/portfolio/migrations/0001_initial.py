# Generated by Django 5.1.3 on 2024-11-16 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('tools', models.CharField(choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('CSS', 'CSS'), ('React', 'React'), ('Django', 'Django'), ('Bootstrap', 'Bootstrap')], default='python', max_length=50)),
                ('date', models.DateField(blank=True, null=True)),
                ('github_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='project_images/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.project')),
            ],
        ),
    ]
