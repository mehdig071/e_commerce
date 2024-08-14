from django.shortcuts import get_object_or_404, render, redirect
from shop.models.Order import Order
import stripe
from django.http import JsonResponse
from shop.services.payment_service import StripeService

def index(request, order_id):
    payment_service = StripeService()
    stripe.api_key = payment_service.get_private_key()
    try:
        order = get_object_or_404(Order, id=order_id)
        amount = int(order.order_cost_ttc *100)
        # Create a PaymentIntent with the order amount and currency
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='eur',
            # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
            automatic_payment_methods={
                'enabled': True,
            },
        )
        
        order.stripe_payment_intent = payment_intent['id']
        order.save()
        
        return JsonResponse({
            'clientSecret': payment_intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({"error": str(e)})



def payment_success(request):
    payment_intent_id = request.GET.get('payment_intent')
    
    if not payment_intent_id:
        # Gérer le cas où 'payment_intent_client_secret' n'est pas présent dans les paramètres GET
        print('Le paramètre payment_intent_client_secret est manquant dans la requête.')
        return redirect('shop:home')
    
    try:
        payment_service = StripeService()
        stripe.api_key = payment_service.get_private_key()
        payment = stripe.PaymentIntent.retrieve(payment_intent_id)
        
        if payment.status == 'succeeded':
            order = get_object_or_404(Order, stripe_payment_intent=payment_intent_id)
            order.is_paid = True
            order.save()
            print('Paiement réussi!')
            return render(request, 'shop/payment_success.html', {})
        else:
            print(f'État du paiement non réussi: {payment.status}')
            return redirect('shop:home')
    except stripe.error.StripeError as e:
        # Gérer les erreurs spécifiques à Stripe
        print(f'Erreur Stripe: {str(e)}')
        return redirect('shop:home')
    except Exception as e:
        # Gérer d'autres exceptions
        print(f'Une erreur s\'est produite: {str(e)}')
        return redirect('shop:home')
