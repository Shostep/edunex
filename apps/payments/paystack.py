"""
Paystack API integration for EduNex
"""
import requests
from django.conf import settings

BASE_URL = "https://api.paystack.co"
HEADERS = {
    'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
    'Content-Type': 'application/json',
}


def initialize_transaction(email, amount_kobo, reference, callback_url, metadata=None):
    """Initialize a new Paystack transaction"""
    data = {
        'email': email,
        'amount': amount_kobo,
        'reference': reference,
        'callback_url': callback_url,
    }
    if metadata:
        data['metadata'] = metadata

    try:
        response = requests.post(
            f"{BASE_URL}/transaction/initialize",
            headers=HEADERS,
            json=data,
            timeout=30
        )
        return response.json()
    except requests.RequestException as e:
        return {'status': False, 'message': str(e)}


def verify_transaction(reference):
    """Verify a Paystack transaction by reference"""
    try:
        response = requests.get(
            f"{BASE_URL}/transaction/verify/{reference}",
            headers=HEADERS,
            timeout=30
        )
        return response.json()
    except requests.RequestException as e:
        return {'status': False, 'message': str(e)}


def verify_connection():
    """Test Paystack API connection"""
    try:
        response = requests.get(
            f"{BASE_URL}/transaction/verify/test",
            headers=HEADERS,
            timeout=10
        )
        return response.status_code == 200 or response.status_code == 404
    except:
        return False
