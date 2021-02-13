from django.shortcuts import render

from .models import Membership


def memberships(request):
    """
    A view to return the memberships page
    """
    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }

    return render(request, 'memberships/memberships.html', context)
