text = input("Inserire una stringa: ")

if len(text) > 10:
    print("Risultato:", text[:10] + "...")
else:
    print("Risultato:", text)
