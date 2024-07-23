
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contactnumber',
            # field=models.IntegerField(max_length=10),
            field=models.BigIntegerField(),

        ),
    ]
