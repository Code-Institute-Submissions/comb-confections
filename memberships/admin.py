from django.contrib import admin
from .models import Membership


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'free_delivery',
        'first_order_disc',
        'overall_discount',
        'monthly_treat',
        'recipe_book',
        'price',
    )
