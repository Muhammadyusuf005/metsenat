from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


from apps.appeals.models import Appeal
from apps.utils.models.base_model import AbstractBaseModel


class StudentSponsor(AbstractBaseModel):
    appeal = models.ForeignKey(
        'appeals.Appeal',
        on_delete=models.PROTECT,
        related_name='sponsored_students',
        limit_choices_to={
            'status': Appeal.AppealStatus.Approved,
        },
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='student_sponsors',
    )
    amount = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0'))],
    )

    def clean(self):
        if self.amount > self.appeal.available_balance:
            raise ValidationError({'message': 'Amount cannot be greater than the appeal available balance.'})
        if self.amount > self.student.balance:
            raise ValidationError({'message': 'Amount cannot be greater than the student\'s available balance.'})

    def save(self, *args, **kwargs):
        self.appeal.available_balance -= self.amount
        self.appeal.save(update_fields=['available_balance'])

        self.student.balance -= self.amount
        self.student.save(update_fields=['balance'])
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.appeal_id} sponsors {self.student_id}"
