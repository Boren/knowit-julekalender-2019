from textwrap import wrap

def main():
    tekst = "tMlsioaplnKlflgiruKanliaebeLlkslikkpnerikTasatamkDpsdakeraBeIdaegptnuaKtmteorpuTaTtbtsesOHXxonibmksekaaoaKtrssegnveinRedlkkkroeekVtkekymmlooLnanoKtlstoepHrpeutdynfSneloietbol"

    # Dei tre første bokstavane bytta plass med dei tre siste.
    # Dei tre neste bytta plass med dei tre nest siste. Og så vidare.
    tekstlist = wrap(tekst, 3)
    tekstlist.reverse()
    tekst = ''.join(tekstlist)

    print(tekst)

    # Første og andre bokstav bytta plass.
    # Tredje og fjerde bokstav bytta plass.
    # Femte og sjette bokstav bytta plass, og så videre for hele lista.
    tekstlist = []

    for i in range(0, len(tekst), 2):
        tekstlist.append(tekst[i+1])
        tekstlist.append(tekst[i])

    tekst = ''.join(tekstlist)

    print(tekst)

    # Lista blei delt i to, og dei to halvdelane bytta plass
    tekst = ''.join([tekst[len(tekst)//2:], tekst[:len(tekst)//2]])
    print(tekst)

if __name__ == "__main__":
    main()