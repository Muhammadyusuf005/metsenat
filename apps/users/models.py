from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.contrib.auth.base_user import BaseUserManager

from apps.general.models import University
from apps.utils.functions import uzbek_phone_validator
from apps.utils.models.base_model import AbstractBaseModel


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field is required")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractUser, AbstractBaseModel):
    class UserRole(models.TextChoices):
        STUDENT = 'student', 'Student'
        SPONSOR = 'sponsor', 'Sponsor'
        ADMIN = 'admin', 'Admin'

    class StudentDegree(models.TextChoices):
        BACHELOR = 'bachelor', 'Bachelor'
        MAGISTER = 'magister', 'Magister'

    class SponsorType(models.TextChoices):
        PHYSICAL = 'physical', 'Physical'
        LEGAL = 'legal', 'Legal'

    email = username = None
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        validators=[uzbek_phone_validator]
    )
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d',
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        blank=True

    )
    degree = models.CharField(
        max_length=10,
        choices=StudentDegree.choices,
        blank=True,
        null=True
    )
    balance = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
        blank=True,
        null=True,
        editable=False
    )
    available_balance = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        default=Decimal('0'),
        validators=[MinValueValidator(Decimal('0'))],
        blank=True,
        null=True,
        editable=False
    )
    university = models.ForeignKey(
        University,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    sponsor_type = models.CharField(
        max_length=20,
        choices=SponsorType.choices,
        blank=True,
        null=True
    )

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def clean(self):

        if self.role == self.UserRole.STUDENT and not self.university:
            raise ValidationError({'message': 'The university is required'})

        if self.role == self.UserRole.STUDENT and not self.degree:
            raise ValidationError({'message': 'The degree is required'})

        if self.role == self.UserRole.STUDENT and self.sponsor_type:
            raise ValidationError({'Student': 'Sponsor type must not be allowed for Students'})

        if self.role == self.UserRole.SPONSOR and not self.sponsor_type:
            raise ValidationError({'sponsor_type': 'The sponsor type is required'})

        if self.role == self.UserRole.SPONSOR and self.university and self.degree:
            raise ValidationError({'sponsor': 'The university and degree must not be allowed'})

        if self.is_superuser :
            self.UserRole = self.UserRole.ADMIN

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number

UserModel = CustomUser