from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
from paytmchecksum import PaytmChecksum
import uuid

# Paytm Settings (Should ideally be in settings.py)
PAYTM_MERCHANT_ID = getattr(settings, 'PAYTM_MERCHANT_ID', 'MID_STAGING_0001')
PAYTM_MERCHANT_KEY = getattr(settings, 'PAYTM_MERCHANT_KEY', '1234567890123456')
PAYTM_WEBSITE = getattr(settings, 'PAYTM_WEBSITE', 'WEBSTAGING')
PAYTM_INDUSTRY_TYPE_ID = getattr(settings, 'PAYTM_INDUSTRY_TYPE_ID', 'Retail')
PAYTM_CHANNEL_ID = getattr(settings, 'PAYTM_CHANNEL_ID', 'WEB')
PAYTM_CALLBACK_URL = getattr(settings, 'PAYTM_CALLBACK_URL', 'http://127.0.0.1:8000/q16/callback/')

import random
import string

def generate_random_patient():
    names = ["Aarav", "Ishaan", "Vihaan", "Aditya", "Arjun", "Ananya", "Diya", "Saanvi", "Kiara", "Myra"]
    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Surat", "Pune", "Jaipur"]
    
    random_name = random.choice(names)
    random_city = random.choice(cities)
    random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    return {
        "name": random_name,
        "city": random_city,
        "patient_id": random_id
    }

def initiate_payment(request):
    # Generate random ID for the session/guest
    if request.method == "GET":
        patient_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        patient_info = {"patient_id": patient_id}
        return render(request, 'Q16/initiate_payment.html', {'patient_info': patient_info})
    
    if request.method == "POST":
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        city = request.POST.get('city')
        patient_id = request.POST.get('patient_id')
        order_id = str(uuid.uuid4())
        
        # User is optional for this practical task
        user = request.user if request.user.is_authenticated else None
        
        # Create a pending transaction
        Transaction.objects.create(
            order_id=order_id,
            amount=amount,
            user=user,
            status='PENDING'
        )

        paytm_params = {
            "MID": PAYTM_MERCHANT_ID,
            "WEBSITE": PAYTM_WEBSITE,
            "INDUSTRY_TYPE_ID": PAYTM_INDUSTRY_TYPE_ID,
            "CHANNEL_ID": PAYTM_CHANNEL_ID,
            "ORDER_ID": order_id,
            "CUST_ID": str(user.id) if user else "GUEST_" + patient_id,
            "MOBILE_NO": "9999999999",
            "EMAIL": user.email if user else "guest@example.com",
            "TXN_AMOUNT": str(amount),
            "CALLBACK_URL": PAYTM_CALLBACK_URL,
        }

        # Generate checksum
        checksum = PaytmChecksum.generateSignature(paytm_params, PAYTM_MERCHANT_KEY)
        paytm_params["CHECKSUMHASH"] = checksum

        return render(request, 'Q16/pay_tm.html', {'paytm_params': paytm_params})

@csrf_exempt
def payment_callback(request):
    if request.method == "POST":
        paytm_params = {}
        for key, value in request.POST.items():
            paytm_params[key] = value
        
        checksum = paytm_params.get('CHECKSUMHASH')
        if checksum:
            paytm_params.pop('CHECKSUMHASH', None)
            
            # Verify signature
            is_valid_checksum = PaytmChecksum.verifySignature(paytm_params, PAYTM_MERCHANT_KEY, checksum)
            
            if is_valid_checksum:
                order_id = paytm_params.get('ORDER_ID')
                txn_id = paytm_params.get('TXNID')
                status = paytm_params.get('STATUS')
                
                try:
                    transaction = Transaction.objects.get(order_id=order_id)
                    transaction.txn_id = txn_id
                    transaction.status = 'SUCCESS' if status == 'TXN_SUCCESS' else 'FAILURE'
                    transaction.save()
                    
                    return render(request, 'Q16/payment_status.html', {
                        'status': transaction.status,
                        'order_id': order_id,
                        'txn_id': txn_id
                    })
                except Transaction.DoesNotExist:
                    return render(request, 'Q16/payment_status.html', {'status': 'ERROR', 'message': 'Transaction not found'})
            else:
                return render(request, 'Q16/payment_status.html', {'status': 'FAILURE', 'message': 'Checksum mismatch'})
                
    return redirect('initiate_payment')
