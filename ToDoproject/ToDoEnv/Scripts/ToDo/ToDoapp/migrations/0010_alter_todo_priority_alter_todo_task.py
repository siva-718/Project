# Generated by Django 4.2.5 on 2023-10-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoapp', '0009_alter_todo_priority_alter_todo_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Priority',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='Task',
            field=models.CharField(max_length=200),
        ),
    ]
