def main():

    summa = 0
    lämpötila2 = 21
    testaukset10 = 0

    # Kysytään testauksien määrä

    rivi = input("Enter the number of measurements: ")
    testaukset = int(rivi)

    # Jos testausten määrä 0 tai alle, annetaan virheilmoitus

    if testaukset < 0 or testaukset == 0:
        print("The number of measurements must be a positive number.")

    #Pyydetään käyttäjältä lämpötilojen arvot ja summataan ne yhteen

    for i in range(1, testaukset+1):
        print("Enter the temperature ", i, ": ", sep="", end="")
        rivi2 = input()
        lämpötila = int(rivi2)
        rivi3 = lämpötila
        summa = summa + lämpötila

        # Tarkistetaan, että kaksi peräkkäistä testausta ei ole rajojen ulkopuolella

        if (lämpötila < 20 and lämpötila2 < 20) or (lämpötila > 25 and lämpötila2 > 25)\
            or (lämpötila < 20 and lämpötila2>25) or (lämpötila2 < 20 and lämpötila >25):
            print("Your wine is ruined.")
            break

        lämpötila2 = int(rivi3)

        # Tarkistetaan, että testauksista yli 10% ei ole lämpötilarajojeä ulkopuolella

        if lämpötila < 20 or lämpötila > 25:
            testaukset10 = testaukset10 + 1
            if testaukset10 > testaukset / 10:
                print("Your wine is ruined.")
                break

        if testaukset == i:
            print("Your wine is ready.")
            break


main()


