class Cozum:
    def romanToInt(self,deger: str) -> int:
        sozluk = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        for char in deger:
            if char not in sozluk:
                print(f"'{char}' geçersiz bir karakterdir.")
                return

            deger = deger.replace("IV", "IIII").replace("IX", "VIIII")
            deger = deger.replace("XL", "XXXX").replace("XC", "LXXXX")
            deger = deger.replace("CD", "CCCC").replace("CM", "DCCCC")

            toplam =0
            for i in deger:
                toplam += sozluk[i]
            return toplam

cozum = Cozum()
bilgiAl = input("Çevirmek istediğiniz Roma rakamını giriniz:")
sonuc = cozum.romanToInt(bilgiAl)
print(f"Girilen Roma rakamı '{bilgiAl}' tam sayı olarak değeri: {sonuc}")