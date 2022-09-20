# Generated by Django 4.1.1 on 2022-09-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_screenshot_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='language',
            field=models.CharField(choices=[('JS', 'Javascript'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('PY', 'Python'), ('NJS', 'Node.js')], default='JS', max_length=10),
        ),
    ]
