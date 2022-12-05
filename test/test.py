import paypalrestsdk
am = input("Enter Amount\n> ")
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "REDACTED_PAYPAL_CLIENT_ID",
  "client_secret": "REDACTED_PAYPAL_SECRET"
})
payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "https://www.paypal.com/payment/PAYID-MODGRTQ7YG77485TE4498349/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "Service",
                "sku": "item",
                "price": int(am),
                "currency": "USD",
                "quantity": 1}]},
        "amount": {
            "total": int(am),
            "currency": "USD"},
        "description": "This is the payment transaction description."}]})

if payment.create():
  print("Payment created successfully")
else:
  print(payment.error)
print(payment.id)
for link in payment.links:
    if link.rel == "approval_url":
        # Convert to str to avoid Google App Engine Unicode issue
        # https://github.com/paypal/rest-api-sdk-python/pull/58
        approval_url = str(link.href)
        print("Click the link to pay:", approval_url)


test = input("test")

payment2 = paypalrestsdk.Payment.find(payment.id)
print(payment2.payer.payer_info.payer_id)
if payment2.execute({"payer_id": payment2.payer.payer_info.payer_id}):
  print("Payment execute successfully")
else:
  print(payment2.error) # Error Hash