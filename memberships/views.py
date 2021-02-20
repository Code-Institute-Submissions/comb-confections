from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Membership
from profiles.models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import User


def memberships(request):
    """
    A view to return the memberships page
    """
    memberships = Membership.objects.all()
    if request.user.is_anonymous:
        context = {
            'memberships': memberships,
        }
    else:
        context = {
            'memberships': memberships,
        }

    return render(request, 'memberships/memberships.html', context)


def membership_type(request):
    """
    Capture membership type selected by user, store it in
    session variable and redirect user to the signup page
    """

    membership_type = request.POST.get('membership_type')
    request.session['membership'] = membership_type
    if request.user.is_authenticated:
        return redirect(reverse('membership_checkout'))

    return redirect(reverse('account_signup'))


@login_required
def membership_checkout(request):
    """
    Retrieve user selected membership, display it and
    benefits, and allow user to change the membership
    type
    """
    # Retrieve data for all memberships
    all_memberships = Membership.objects.all()

    # Check if user already has a memership and got to this
    # page by accident, then re-direct to change site
    profile = UserProfile.objects.get(user=request.user)
    if profile.membership:
        return redirect(reverse('membership_change'))
    # If user is updating selected membership, the
    # memberhip_type to the new value
    if request.GET.get('membership-new'):
        membership_type = request.GET.get('membership-new')
        # add membership type to session to retrieve for stripe
        request.session['membership'] = membership_type
    # If user logged in after
    # registering, get membership_type from session
    else:
        try:
            # Retrieve user selected membership
            membership_type = request.session['membership']
        except KeyError:
            # If user logged in normally, redirect them
            # to the profile page
            return redirect(reverse('products'))

    # Retrieve data for selected membership type
    membership = get_object_or_404(Membership, name=membership_type)

    template = 'memberships/membership_checkout.html'
    context = {
        'membership': membership,
        'all_memberships': all_memberships,
    }

    return render(request, template, context)


@login_required
def user_membership_view(request):
    """
    Displays user's membership view with details
    """
    profile = UserProfile.objects.get(user=request.user)

    if not profile.membership:
        messages.error(request, "You haven't subscribed to a membership yet. "
                                " Choose one and join the Prickly fam")
        return redirect(reverse('memberships'))

    membership = get_object_or_404(Membership, name=profile.membership)
    context = {
        'membership': membership,
    }
    template = 'memberships/user_membership.html'

    return render(request, template, context)


@login_required
def membership_change(request):
    """
    Handles membership change and adding selected memebrship
    to the session
    """
    profile = UserProfile.objects.get(user=request.user)
    if not profile.membership:
        return redirect(reverse('memberships'))

    if not request.POST.get('membership_type'):
        return redirect(reverse('memberships'))

    all_memberships = Membership.objects.all()
    membership_type = request.POST.get('membership_type')
    request.session['membership'] = membership_type
    membership = get_object_or_404(Membership, name=membership_type)
    template = 'memberships/membership_checkout.html'

    context = {
        'change_membership': True,
        'membership': membership,
        'all_memberships': all_memberships,
    }
    return render(request, template, context)
