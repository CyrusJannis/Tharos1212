from paypalrestsdk import Payout, ResourceNotFound
import paypalrestsdk
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "Afb5y5r--lsY8PBMXCqUQupMbgE8dopgQDu0mvHccXkw_d2DDL7rYEiJsbGQ1h5ACS_lTbLFR9FDsGol",
  "client_secret": "EKzQLSO1hBHqgjqFhHlbr-ETAJtgOYD3vSYS32Bpk5IIT7AGL4KGR5WBthSVmkdvLytP4c0Z9xjijot4"
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
                "value": 0.09,
                "currency": "USD"
            },
            "receiver": "sleathbots@gmail.com",
            "note": "Thank you.",
            "sender_item_id": "item_1"
        }
    ]
})

try:
    payout.create()
    print("payout created successfully")
except Exception as e:
    print(payout.error, e)