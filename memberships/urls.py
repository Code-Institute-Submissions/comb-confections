from django.urls import path
from . import views


urlpatterns = [
    path('', views.memberships, name="memberships"),
    path('membership_type/', views.membership_type,
         name='membership_type'),
    path('membership_checkout/', views.membership_checkout,
         name="membership_checkout"),
    path('user_membership/', views.user_membership_view,
         name="user_membership"),
    path('membership_change/', views.membership_change,
         name="membership_change"),
    path('membership_update/', views.membership_change,
         name="membership_update"),
    path('cancel_membership/', views.cancel_membership,
         name="cancel_membership"),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('membership_success/', views.membership_success),
    path('webhook/', views.stripe_webhook),
]
