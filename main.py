#OKJ vizsgafeladat gyakorlás
#https://infojegyzet.hu/vizsgafeladatok/okj-programozas/szoftverfejleszto-190514/

from Fuvarok import Fuvarok

def main():
    #1-2 feladat megvalósítva a Fuvar és Fuvarok osztályban
    f = Fuvarok(r"fuvar.csv")
    
    #További segédfüggvények a Fuvarok osztályban
    #3.feladat
    print(f"3.feladat: { len(f.fuvar_list) } fuvar")

    #4.feladat
    print(f"4.feladat: { len(f.get_fuvars_by_id(6185)) } fuvar alatt: { f.get_sum_of_money(f.get_fuvars_by_id(6185)) }$")

    #5.feladat
    print(f"5.feladat:")
    local_dict = f.statistic()
    for key, value in local_dict.items():
        string = "\t" + key + ": " +  str(value) + " fuvar"
        print(string.replace("\n", ""))
    
    #6.feladat
    print(f"6.feladat: { round(f.get_all_km() * 1.6, 2) }")
    longest_fuvar = f.get_longest_fuvar()

    #7.feladat
    print(f"""7.feladat: Leghosszabb fuvar:
    Fuvar hossza: { longest_fuvar.tavolsag } másodperc
    Taxi azonosító: { longest_fuvar.taxi_id }
    Megtett távolság: { str(round(longest_fuvar.tavolsag, 1)).replace(".", ",") }
    Viteldíj: { str(longest_fuvar.viteldij).replace(".", ",") }$""")

    #8.feladat
    f.write_errors()

if __name__ == "__main__":
    main()