from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_blogpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_modified',
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создано'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='modified_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Изменено'),
            preserve_default=False,
        ),
    ]
