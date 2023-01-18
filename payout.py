import paypalrestsdk
from paypalrestsdk import Payout, ResourceNotFound
paypalrestsdk.configure({
    "mode": "live", # sandbox or live
    "client_id": "REDACTED_PAYPAL_CLIENT_ID",
    "client_secret": "REDACTED_PAYPAL_SECRET"
})

payout = Payout({
    "sender_batch_header": {
        "sender_batch_id": "batch_1",
        "email_subject": "You have a payment"
    },
    "items": [
        {
            "recipient_type": "EMAIL",
            "amount": {
                "value": 0.1,
                "currency": "USD"
            },
            "receiver": "sleathbots@gmail.com",
            "note": "Thank you.",
            "sender_item_id": "item_1"
        }
    ]
})

if payout.create():
    print("Payout worked")
else:
    print(payout.error)