print('Enter the age of your dog:') # Ausgabe
dog_age = int(input()) # Eingabe als integer
if dog_age <=0:
    print("Falsche Angabe")
elif dog_age==1:
    print("Dein Hund ist 14 Menschenjahre alt")
elif dog_age==2:
    print("Dein Hund ist 22 Menschenjahre alt")
else:
    h = (dog_age-2)*5+22
    print("Dein Hund ist ", h," Menschenjahre alt ")