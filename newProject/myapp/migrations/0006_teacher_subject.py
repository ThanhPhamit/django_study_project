# Generated by Django 4.1.7 on 2023-02-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_menu_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('TeacherID', models.IntegerField(primary_key=True, serialize=False)),
                ('Qualification', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('Subjectcode', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('credits', models.IntegerField()),
                ('teacher', models.ManyToManyField(to='myapp.teacher')),
            ],
        ),
    ]
