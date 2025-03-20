from django.db import models
from django.core.exceptions import ValidationError
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    is_show = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="products")

   
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    quantity = models.PositiveIntegerField(default=1)  
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0) 
    worker_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    other_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  
    single_piece_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0.0)

    def clean(self):
        """Validate that either discount_percent or discount_price is provided, not both"""
        if self.discount_percent and self.discount_price:
            raise ValidationError("use only dicount price or percent")

    def save(self, *args, **kwargs):
        
        if self.quantity > 0:
            total_cost = self.buying_price + self.rent_cost + self.worker_cost + self.other_cost + self.profit
            self.single_piece_price = total_cost / self.quantity
        else:
            self.single_piece_price = 0.0
        super().save(*args, **kwargs)

    def get_final_price(self):
        """Return the final price after discount"""
        if self.discount_price:
            return self.price - self.discount_price
        elif self.discount_percent:
            discount_amount = (self.price * self.discount_percent) / 100
            return self.price - discount_amount
        else:
            return self.price

    def __str__(self):
        return self.name
    
class Offer(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='offers/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
