#1) შექმენით სია რომელშიც იქნება მინიმუმ 10 სახელი შემდეგ ამ სიიდან ამოშალეთ ისეთი სახელები რომლის სიგრძეც იქნება
#  10ზე მეტი და დააბრუნეთ გაფილტრული სია გამოიყენეთ for loop და ნასწავლი ფუნქციები


names = ["giorgi", "dato wiklauri", "vano", "nika choquri", "gabrieli", "maia", "mariam chiqovani",
          "eliko", "jemala", "jemala2"]
gapiltruli_sia = []

for name in names:
    if len(name) < 10:
        gapiltruli_sia.append(name)
        print(name)