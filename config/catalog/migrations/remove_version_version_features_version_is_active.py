from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='version_features',
        ),
        migrations.AddField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активна'),
        ),
    ]
