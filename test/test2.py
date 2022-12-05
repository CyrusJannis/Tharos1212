import paypalrestsdk
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "REDACTED_PAYPAL_CLIENT_ID",
  "client_secret": "REDACTED_PAYPAL_SECRET"
})
payment = paypalrestsdk.Payment.find("PAYID-MODGMSY8B5149472W964964N")
print(payment.state)