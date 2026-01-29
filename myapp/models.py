from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories/", blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default="Telangana")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("city", "area")

    def __str__(self):
        return f"{self.area}, {self.city}"

# class Vendor(models.Model):
#     org_name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=255, unique=True, blank=True)
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         related_name="vendors"
#     )
#
#     location = models.ForeignKey(
#         Location,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name="vendors"
#     )
#
#     contact_no = models.CharField(max_length=20)
#     email = models.EmailField(blank=True, null=True)
#     website = models.URLField(blank=True, null=True)
#
#     google_maps_link = models.URLField(blank=True, null=True)
#
#     services = models.TextField(
#         help_text="Comma separated services"
#     )
#
#     materials = models.TextField(
#         blank=True,
#         help_text="Comma separated materials"
#     )
#
#     price_min = models.PositiveIntegerField(null=True, blank=True)
#     price_max = models.PositiveIntegerField(null=True, blank=True)
#
#     PRICE_UNIT_CHOICES = [
#         ("sqft", "Per Sqft"),
#         ("visit", "Per Visit"),
#         ("day", "Per Day"),
#         ("ton", "Per Ton"),
#     ]
#
#     price_unit = models.CharField(
#         max_length=20,
#         choices=PRICE_UNIT_CHOICES,
#         blank=True
#     )
#
#     google_rating = models.FloatField(null=True, blank=True)
#
#     poc_name = models.CharField(max_length=100, blank=True)
#
#     verified = models.BooleanField(default=False)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True)
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             base_slug = slugify(self.org_name)
#             slug = base_slug
#             counter = 1
#
#             while Vendor.objects.filter(slug=slug).exists():
#                 slug = f"{base_slug}-{counter}"
#                 counter += 1
#
#             self.slug = slug
#
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.org_name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} → {self.name}"
class Vendor(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    org_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    contact_no = models.CharField(max_length=20)

    services = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.org_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.org_name

class VendorPhoto(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        related_name="photos",
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to="vendor_photos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo - {self.vendor.org_name}"
