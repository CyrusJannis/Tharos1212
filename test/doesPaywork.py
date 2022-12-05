id = "1212212122"
start = True
n = 0
status = "test"
while start:
    if str(id) + str(n) in data:
        if status == 0:
            await send("Complete other prject first")
        else:
            n +=1
            continue
    else:
        daten eintragen
        start = False