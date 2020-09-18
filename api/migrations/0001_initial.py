from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user=CustomUser(name="unreal",
        email="patelr4142@gmail.com",
        is_staff=True,
        is_superuser=True,
        phone="9574714884",
        gender="Male")
        user.set_password("rahul4884")
        user.save()
    
    dependencies=[

    ]

    oprations=[
        migrations.RunPython(seed_data),
    ]  