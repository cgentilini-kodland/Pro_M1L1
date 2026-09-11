word = input("Inserisci una parola: ")
vowels = "aeiouAEIOU"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print("Numero di vocali:", count)

