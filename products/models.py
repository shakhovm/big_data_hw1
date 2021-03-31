from django.db import models


class Product(models.Model):
    id = models.\
        CharField(verbose_name='id', db_index=True, max_length=60, primary_key=True)
    product_parent = models.IntegerField()
    product_title = models.CharField(max_length=500)
    product_category = models.CharField(max_length=60)

    class Meta:
        db_table = 'products'
