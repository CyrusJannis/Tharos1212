import paypalrestsdk
paypalrestsdk.configure({
  "mode": "live", # sandbox or live
  "client_id": "Afb5y5r--lsY8PBMXCqUQupMbgE8dopgQDu0mvHccXkw_d2DDL7rYEiJsbGQ1h5ACS_lTbLFR9FDsGol",
  "client_secret": "EKzQLSO1hBHqgjqFhHlbr-ETAJtgOYD3vSYS32Bpk5IIT7AGL4KGR5WBthSVmkdvLytP4c0Z9xjijot4"
})
payment = paypalrestsdk.Payment.find("PAYID-MODGMSY8B5149472W964964N")
print(payment.state)