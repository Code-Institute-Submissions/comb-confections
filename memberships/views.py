from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)

from .models import Membership


def memberships(request):
    """
    A view to return the memberships page
    """

    # Get all membership model entries
    memberships = Membership.objects.all()
    template = 'memberships/memberships.html'
    if request.user.is_anonymous:
        context = {
            'memberships': memberships,
        }
    # else:
        # profile = Profile.objects.get(user=request.user)
        # if profile.membership:
        #    user_membership = profile.membership.name
        #    context = {
        #       'user_membership': user_membership,
        #        'memberships': memberships,
        #    }
        # else:
        #    context = {
        #       'memberships': memberships,
        #    }

    return render(request, template, context)

    return HttpResponse(status=200)
