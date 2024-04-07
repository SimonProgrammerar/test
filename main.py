def main():
  # Skapa en tom lista för att lagra namn och tider
  deltagare = []

  # Låt användaren mata in antalet deltagare
  antal_deltagare = int(input("Ange antalet deltagare: "))

  # Låt användaren mata in namn och tid för varje deltagare
  for i in range(1, antal_deltagare + 1):
      namn = input(f"Ange namn för deltagare {i}: ")
      tid = float(input(f"Ange tid för {namn} (i sekunder): "))
      deltagare.append((namn, tid))

  # Sortera deltagarna baserat på tiden (snabbast först)
  deltagare.sort(key=lambda x: x[1])

  # Tilldela poäng enligt den givna regeln
  poäng = 40
  for placering, (namn, tid) in enumerate(deltagare, start=1):
      print(f"{placering}. {namn}: {poäng} poäng")
      poäng -= 1

if __name__ == "__main__":
  main()