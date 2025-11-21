from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def to_dict(self) -> dict:
        return {
            "id": self.pk,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def to_dict(self) -> dict:
        return {
            "id": self.pk,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "stock": self.stock,
            "is_active": self.is_active,
            "category": self.category.to_dict() if self.category else None,
            "images": [img.to_dict() for img in self.images.all()],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_pics/')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    alt_text = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def to_dict(self) -> dict:
        return {
            "id": self.pk,
            "url": self.image.url,
            "alt_text": self.alt_text,
            "created_at": self.created_at.isoformat()
        }

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Image for {self.product.name}'
