from django.conf import settings
from django.db import models

STATUS_CHOICES = (("IN_STOCK", "In Stock"), ("OUT_OF_STOCK", "Out Of Stock"))

ORDER_BY_CHOICES = (
    ("cost_asc", "Cost Asc"),
    ("cost_desc", "Cost Desc"),
    ("max_count", "Max Count"),
    ("max_cost", "Max Cost"),
)


class Product(models.Model):
    title = models.CharField(max_length=200)
    cost = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="IN_STOCK"
    )
    description = models.TextField(default="")


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    count = models.IntegerField()
