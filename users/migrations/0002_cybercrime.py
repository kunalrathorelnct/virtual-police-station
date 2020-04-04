# Generated by Django 2.2.5 on 2020-01-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CyberCrime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_report', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('report_anonomous', models.BooleanField(default=False)),
                ('anonomous_info', models.CharField(blank=True, max_length=200, null=True)),
                ('name_of_victim', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('datetime_of_incidence', models.DateTimeField(blank=True, null=True)),
                ('occurence_of_incidence', models.CharField(blank=True, max_length=200, null=True)),
                ('your_knowledge_of_incidence', models.CharField(blank=True, max_length=100, null=True)),
                ('identified_accused', models.CharField(blank=True, max_length=100, null=True)),
                ('description_of_incidence', models.TextField(blank=True, null=True)),
                ('other_info', models.TextField(blank=True, null=True)),
            ],
        ),
    ]