from django.contrib.auth.models import AbstractUser

# Create your models here.
class AccountModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    
