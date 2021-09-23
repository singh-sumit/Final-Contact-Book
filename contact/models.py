from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    mid_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20)

    is_available = models.BooleanField(default=False)

    # phone = models.ForeignKey(PhoneDetail, on_delete=models.CASCADE, related_name="phone_holder")
    # email = models.ForeignKey(EmailAccount, on_delete=models.CASCADE, related_name="email_holder")


class EmailAccount(models.Model):
    email = models.EmailField(blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="email_set")


# Phone Label
PHONE_LABEL = (
    ('mobile', "Mobile"),
    ('home', "Home"),
    ("work", "Work"),
    ("main", "Main"),
    ("fax", "Fax"),
)


class PhoneDetail(models.Model):
    # area_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=10, )
    label = models.CharField(max_length=10, choices=PHONE_LABEL, default=PHONE_LABEL[0][0])
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="phone_set")
