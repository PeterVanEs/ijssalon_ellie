def presenteer(tabel, totaal):
    #print(tabel)
    for k, v in tabel.items():
        print(f"{k} : {v} euro")
    print("=" * 26)
    print(f"Totaal : {totaal} euro")
