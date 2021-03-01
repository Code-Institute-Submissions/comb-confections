from django.db import models
from django.contrib.auth.models import User


class Membership(models.Model):
    """
    Creates a membership model containing details
    of each different membership
    """
    YES = 'Y'
    NO = 'N'
    RECIPE_BOOK = [
        (YES, 'Yes'),
        (NO, 'No')
    ]

    YES = 'Y'
    NO = 'N'
    FREE_DELIVERY = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(
        'Membership Image', null=True, blank=True)
    free_delivery = models.CharField(max_length=1,
                                     choices=FREE_DELIVERY,
                                     default='N')
    first_order_disc = models.IntegerField('First Order Discount', default=0)
    overall_discount = models.IntegerField(default=0)
    monthly_treat = models.CharField(
        'Monthly Treat', max_length=50,
        null=True, blank=True)
    recipe_book = models.CharField(max_length=10,
                                   choices=RECIPE_BOOK, default='N')
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.usernameWhen
