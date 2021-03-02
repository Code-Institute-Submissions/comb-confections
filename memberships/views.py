import stripe

from django.conf import settings

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Membership, StripeCustomer
from profiles.models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import User


def memberships(request):
    """
    Membership Page
    """

    # Get all membership model entries
    memberships = Membership.objects.all()
    template = 'memberships/memberships.html'
    if request.user.is_anonymous:
        context = {
            'memberships': memberships,
        }
    else:
        profile = UserProfile.objects.get(user=request.user)
        if profile.membership:
            user_membership = profile.membership.name
            context = {
                'user_membership': user_membership,
                'memberships': memberships,
            }
        else:
            context = {
                'memberships': memberships,
            }

    return render(request, template, context)


def membership_type(request):
    """
    Capture membership type selected by user.
    """

    membership_type = request.POST.get('membership_type')
    request.session['membership'] = membership_type
    if request.user.is_authenticated:
        return redirect(reverse('membership_checkout'))

    return redirect(reverse('account_signup'))


@login_required
def membership_checkout(request):
    """
    Retrieve selected membership option, display
    benefits, and allow user to change membership.
    """
    # Retrieve data for all memberships
    types_of_memberships = Membership.objects.all()

    profile = UserProfile.objects.get(user=request.user)
    if profile.membership:
        return redirect(reverse('membership_change'))

    if request.GET.get('membership-new'):
        membership_type = request.GET.get('membership-new')
        request.session['membership'] = membership_type
    else:
        try:
            membership_type = request.session['membership']
        except KeyError:
            return redirect(reverse('products'))

    # Retrieve data for selected membership type
    membership = get_object_or_404(Membership, name=membership_type)

    template = 'memberships/membership_checkout.html'
    context = {
        'membership': membership,
        'types_of_memberships': types_of_memberships,
    }

    return render(request, template, context)


@login_required
def user_membership_view(request):
    """
    Displays user's membership view with details
    """
    profile = UserProfile.objects.get(user=request.user)

    if not profile.membership:
        messages.error(
            request, "You haven't treated yourself to a membership yet.")
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
    Handles membership change
    """
    profile = UserProfile.objects.get(user=request.user)
    if not profile.membership:
        return redirect(reverse('memberships'))

    if not request.POST.get('membership_type'):
        return redirect(reverse('memberships'))

    types_of_memberships = Membership.objects.all()
    membership_type = request.POST.get('membership_type')
    request.session['membership'] = membership_type
    membership = get_object_or_404(Membership, name=membership_type)
    template = 'memberships/membership_checkout.html'

    context = {
        'change_membership': True,
        'membership': membership,
        'types_of_memberships': types_of_memberships,
    }
    return render(request, template, context)


@login_required
def cancel_membership(request):
    if not UserProfile.objects.get(user=request.user).membership:
        return redirect(reverse('memberships'))

    stripe.api_key = settings.STRIPE_SECRET_KEY
    # user's membership
    membership = get_object_or_404(Membership, name=profile.membership)
    profile = get_object_or_404(UserProfile, user=request.user)
    profile.membership = membership

    try:
        stripe.Subscription.delete(profile.membership)
    except Exception as e:
        return JsonResponse({'error': (e.args[0])}, status =403)

    return redirect("products")


@login_required
def membership_update(request):
    """
    Update user's membership
    """
    print("ENTERING UPDATE FUNCTION")
    if not UserProfile.objects.get(user=request.user).membership:
        print("NO MEMBERSHIP")
        return redirect(reverse('memberships'))

    stripe.api_key = settings.STRIPE_SECRET_KEY
    # user's membership
    membership = request.session['membership']

    # Asign correct prices to the paid memberships
    if membership == 'Queen_Bee':
        price = settings.STRIPE_PRICE_ID_QUEEN_BEE
    elif membership == 'Supreme Bee':
        price = settings.STRIPE_PRICE_ID_DRONE_BEE
    elif membership == 'Worker_Bee':
        price = settings.STRIPE_PRICE_ID_WORKER_BEE
    else:
        price = settings.STRIPE_PRICE_ID_BEEHIVE

    # Check if the user already exists in stripe system and
    # our database
    try:
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        subscription = stripe.Subscription.retrieve(
            stripe_customer.stripeSubscriptionId)
        # Update existing membership with a new one
        stripe.Subscription.modify(
            subscription.id,
            cancel_at_period_end=False,
            proration_behavior='create_prorations',
            items=[{
                'id': subscription['items']['data'][0].id,
                'price': price,
            }]
        )

        # Attach new membership to the user's profile
        membership_type = get_object_or_404(Membership, name=membership)
        profile = get_object_or_404(UserProfile, user=request.user)
        profile.membership = membership_type
        profile.save()

        messages.success(request, 'Congrats!! You successfully changed '
                                  'to the f{membership} membership!')
        # Redirect the user to profiles page
        return redirect(reverse('profile'))

    # If user doesn't exist, return error
    except StripeCustomer.DoesNotExist:
        return messages.error(request, 'User does not exist')


@csrf_exempt
def stripe_config(request):
    """
    Handles AJAX requests coming from main.js
    """
    if request.method == 'GET':
        # add public key in a dict that will be retrieved by JS
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    price = settings.STRIPE_PRICE_ID_QUEEN_BEE
    price = settings.STRIPE_PRICE_ID_DRONE_BEE
    price = settings.STRIPE_PRICE_ID_WORKER_BEE
    price = settings.STRIPE_PRICE_ID_BEEHIVE
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'GET':

        domain_url = 'https://8000-f474b91f-1d9f-4350-ab85-ee68d90ad8a1.ws-eu03.gitpod.io/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        membership = request.session['membership']

        if membership == 'Queen_Bee':
            price = settings.STRIPE_PRICE_ID_QUEEN_BEE
        elif membership == 'Drone_Bee':
            price = settings.STRIPE_PRICE_ID_DRONE_BEE
        elif membership == 'Worker_Bee':
            price = settings.STRIPE_PRICE_ID_WORKER_BEE
        else:
            price = settings.STRIPE_PRICE_ID_BEEHIVE

        try:
            # Create a Checkout Session
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=(request.user.id if
                                     request.user.is_authenticated else None),
                success_url=(
                    domain_url + (
                        'memberships/membership_success?session_id={CHECKOUT_SESSION_ID}')),
                cancel_url=domain_url + 'memberships/membership_checkout/',
                payment_method_types=['card'],
                # Subscription model
                mode='subscription',
                line_items=[
                    {
                        'price': price,
                        'quantity': 1,
                    }
                ]
            )
            # Return Checkout Session ID
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def membership_success(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if not profile.membership:
        membership_type_value = request.session['membership']
        membership_type = Membership.objects.get(name=membership_type_value)
        profile.membership = membership_type
        profile.save()

    membership = (
        get_object_or_404(UserProfile, user=request.user).membership.name)

    # Add a success message
    messages.success(request, 'Congrats!! You successfully'
                              ' subscribed to the '
                              f'{membership} membership!')
    # Redirect the user to profiles page
    return redirect(reverse('profile'))


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        total = session.get('amount_total')
        total_num = round(total / 100, 2)
        # get membership type based on the price
        membership_type = get_object_or_404(Membership, price=total_num)

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
        profile = get_object_or_404(UserProfile, user=user)
        profile.membership = membership_type
        profile.save()

    return HttpResponse(status=200)
