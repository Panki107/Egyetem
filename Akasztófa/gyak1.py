import sys

def main():
    orszagok = {}
    with open("oszagok.txt", encoding="utf-8") as file:
        for line in file:
            adatok = line.strip().split(";")
            if adatok[0] in orszagok:
                orszagok[adatok[0]] += int(adatok[2])
            else:
                orszagok[adatok[0]] = int(adatok[2])
        for kulcs, ertek in sorted(orszagok.items(), key=lambda rend: (-rend[1], rend[0])):
            print(f"{kulcs},{ertek}")

if __name__ == '__main__':
    main()