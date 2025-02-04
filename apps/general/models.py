from decimal import Decimal
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from apps.utils.models.base_model import AbstractBaseModel


class PaymentMethod(AbstractBaseModel):
    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the name of the payment method."
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        editable=False,
        verbose_name="Slug"
    )

    def clean(self):
        existing_slugs = PaymentMethod.objects.values_list('slug', flat=True)
        generated_slug = slugify(self.name)
        if generated_slug in existing_slugs:
            raise ValidationError({"name": "This payment method already exists."})
        self.slug = generated_slug

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class University(AbstractBaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="University Name"
    )
    contract_amount = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name="Contract Amount"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        editable=False,
        verbose_name="Slug"
    )

    def clean(self):
        existing_slugs = University.objects.values_list("slug", flat=True)
        generated_slug = slugify(self.name)

        if generated_slug in existing_slugs:
            raise ValidationError({"name": "This university already exists."})

        self.slug = generated_slug

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
