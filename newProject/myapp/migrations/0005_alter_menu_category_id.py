# Generated by Django 4.1.7 on 2023-02-22 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_menu_menucategory_delete_person_menu_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='category_name', to='myapp.menucategory'),
        ),
    ]
