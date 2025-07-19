from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    daily_rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True, null=True, upload_to="products/")
    is_available = models.BooleanField(default=True)
    seats = models.PositiveIntegerField(default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        ordering = ['brand', 'model', 'year']
