import math

def volume_tabung(diameter, tinggi):
    return math.pi * (diameter / 2)**2 * tinggi

def volume_kubus(sisi):
    return sisi**3

def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def main():
    print("==================== KALKULATOR CERDAS ====================")
    print("Pilihlah bangun yang ingin anda hitung (inputan angka saja):")
    print("1. Tabung")
    print("2. Kubus")
    print("3. Balok")
    
    pilihan = input(">> ")
    
    if pilihan == "1":
        diameter, tinggi = float(input("Masukkan diameter(cm): ")), float(input("Masukkan tinggi(cm): "))
        hasil = volume_tabung(diameter, tinggi)
        print(f"Volume tabung adalah {hasil:.2f} cm")
    elif pilihan == "2":
        sisi = float(input("Masukkan sisi(cm): "))
        hasil = volume_kubus(sisi)
        print(f"Volume kubus adalah {hasil:.2f} cm")
    elif pilihan == "3":
        panjang, lebar, tinggi = float(input("Masukkan panjang(cm): ")), float(input("Masukkan lebar(cm): ")), float(input("Masukkan tinggi(cm): "))
        hasil = volume_balok(panjang, lebar, tinggi)
        print(f"Volume balok adalah {hasil:.2f} cm")
    else:
        print("Inputan yang anda masukkan salah !!")

if __name__ == "__main__":
    main()
