import unicodedata as ucd
msg = "\u3000asasdadadadaasd"
res=ucd.normalize('NFKC', msg).replace(' ', '')
print(msg)

