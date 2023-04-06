from django.db import models

# Create your models here.
# model
class Product(models.Model):
    class Meta:
        db_table = "product"

    code = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=128, null=False)
    description = models.TextField(max_length=300, null=False)
    price = models.IntegerField(null=False, default=0)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

    # def __str__(self):
    #     return self.code

    # def save(self, *args, **kwargs):