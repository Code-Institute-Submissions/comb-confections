from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from memberships.models import Membership
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if not profile.membership:
        messages.error(request, "You haven't subscribed to a membership yet.")
        return redirect(reverse('memberships'))

    membership = get_object_or_404(Membership, name=profile.membership)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Something went wrong. '
                                    'Try again and make sure all '
                                    'fields are valid!')
    else:
        form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'membership': membership,
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'profile': profile,
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def order_details(request, order_id):
    """
    Retrieves specific order details
    """
    # Get the order
    order = get_object_or_404(Order, pk=order_id)
    # Calculate the discount
    discount = round((order.subtotal - (order.total - order.delivery_cost)) /
                     order.subtotal * 100, 0)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'discount': discount,
        'order_details': True,
    }

    return render(request, template, context)
