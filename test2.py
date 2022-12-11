with open("main.py", 'r') as fp:
    a = len(fp.readlines())
with open("test.py", 'r') as fp:
    b = len(fp.readlines())
with open("./cogs/Verify.py", 'r') as fp:
    c = len(fp.readlines())
with open("./cogs/Registerasanexpert.py", 'r') as fp:
    d = len(fp.readlines())
with open("./cogs/Postajob.py", 'r') as fp:
    e = len(fp.readlines())
with open("./cogs/Offerwork.py", 'r') as fp:
    f = len(fp.readlines())
with open("./cogs/db/chats.json", 'r') as fp:
    g = len(fp.readlines())
with open("./cogs/db/delete_messages.json", 'r') as fp:
    h = len(fp.readlines())
with open("./cogs/db/eqs_questions.json", 'r') as fp:
    i = len(fp.readlines())
with open("./cogs/db/expertzahlinfos.json", 'r') as fp:
    j = len(fp.readlines())
with open("./cogs/db/finanzen.json", 'r') as fp:
    k = len(fp.readlines())
with open("./cogs/db/payments.json", 'r') as fp:
    l = len(fp.readlines())
with open("./cogs/db/wasgeht.json", 'r') as fp:
    m = len(fp.readlines())
print(a + b + c + d + e + f + g + h + i + j + k + l + m)