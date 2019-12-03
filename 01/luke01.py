def main():
    SAUFIL = 'sau.txt'

    dragestørrelse = 50
    sauebeholdning = 0
    dager_uten_mat = 0
    dag = 0

    with open(SAUFIL) as f:
        sauer = map(int, f.read().split(','))

    for sau in sauer:
        sauebeholdning += sau
        sauebeholdning -= dragestørrelse

        if sauebeholdning >= 0:
            dragestørrelse += 1
            dager_uten_mat = 0
        else:
            dragestørrelse -= 1
            sauebeholdning = 0
            dager_uten_mat += 1

        if dager_uten_mat == 5:
            print(f"Landbyen overlevde {dag} dager")
            exit(0)

        dag += 1

if __name__ == "__main__":
    main()