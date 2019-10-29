print ""
print "MRH tool v-1.5 by Habibi"
print ""
print "pilih dengan hati-hati! "
print ""
print "jangan disalah gunakan guys :) "
print ""
print "untuk no 2 belum lengkap"
print ""
print "-----TOOLS MENU-----"
print "[1] Mencari hasil bilangan berpangkat"
print "[2] Rumus dan kisi-kisi UN MATEMATIKA SMP 2020"
print "[3] Kontak admin"
print "[4] Mencari faktor sebuah bilangan"
print ""
pilih=raw_input("Masukkan nomor yang ingin dipilih! ")
if pilih == "1":
    print ""
    num1 = input("Masukkan bilangan = ")
    num2 = input("Masukkan pangkat ")
    print num1, "pangkat", num2, "adalah", num1 ** num2
elif pilih == "2":
    print ""
    print "SUMBER : BUKU DETIK-DETIK UN SMP MTK"
    print ""
    print "[1] Perbandingan"
    print "[2] Aritmerika sosial"
    print "[3] Operasi hitung bentuk akar"
    print "[4] Bentuk aljabar"
    print ""
    pilih=raw_input("Masukkan nomor yang ingin dipilih! ")
    if pilih == "1":
        print ""
        print "Jumlah dan selisih perbandingan"
        print ""
        print "Jumlah perbandingan :"
        print ""
        print "A = a : (a+b) x (A + B)"
        print ""
        print ""
        print "B = b : (a+b) x (A + B)"
        print ""
        print ""
        print "Selisih perbandingan :"
        print ""
        print "A = a : (a-b) x (A - B)"
        print ""
        print ""
        print "B = b : (a-b) x (A - B)"
    elif pilih == "2":
        print ""
        print "[1] Mencari nilai keseluruhan, nilai satuan "
        print"    dan nilai sebagian"
        print "[2] Mencari presentase untung dan rugi"
        print "[3] Diskon, bruto, neto dan tara"
        print "[4] Bunga tunggal "
        print "[5] Angsuran"
        pilih = raw_input("Masukkan nomor yang ingin dipilih! ")
        if pilih == "1":
            print ""
            print "1.nilai keseluruhan = "
            print ""
            print "  banyak unit x nilai per unit"
            print ""
            print "2.nilai satuan ="
            print ""
            print "  nilai keseluruhan : banyak satuan"
            print ""
            print "3.nilai sebagian ="
            print ""
            print "  banyak bagian satuan x nilai satuan"
            print ""
        elif pilih == "2":
            print ""
            print "1.Presentase untung = "
            print ""
            print "  untung : harga pembelian x 100%"
            print ""
            print "2.Presentase rugi ="
            print ""
            print "  rugi : harga pembelian x 100%"
        elif pilih == "3":
            print ""
            print "tara = bruto-neto"
            print "neto = bruto-tara"
            print "bruto = neto + tara"
            print ""
            print ""
            print "NOTE ="
            print "1.Diskon = potongan harga yang diberikan"
            print "2.Bruto = berat barang/berat seluruhnya"
            print "3.Neto = jumlah/berat suatu barang"
            print "4.Tara = potongan jumlah atau berat"
            print "  barang karena adanya berat pembungkus/kemasan"
        elif pilih == "4":
            print ""
            print "COMING SOON ! SILAHKAN HUBUNGI ADMIN "
            print "WA = +62852 1707 8508"
            print "INSTAGRAM = @raghibhabibi"
        elif pilih == "5":
            print ""
            print "angsuran = "
            print ""
            print "(pinjaman semula + bunga) : lama pelunasan"
            print ""
        else:
            print "input salah, harap coba lagi"
    elif pilih == "3":
        print ""
        print "COMING SOON ! SILAHKAN HUBUNGI ADMIN "
        print "WA = +62852 1707 8508"
        print "INSTAGRAM = @raghibhabibi"
    elif pilih == "4":
        print ""
        print "[1] Unsur-unsur pada aljabar"
        print "[2] Operasi bentuk aljabar"
        print "[3] Pemfaktoran bentuk aljabar"
        print ""
        pilih = raw_input("Masukkan nomor yang ingin dipilih! ")
        if pilih == "1":
            print ""
            print "1. Variabel/perubah"
            print "  yaitu simbol-simbol yang mewakili suatu bilangan pada "
            print "  suatu bentuk aljabar"
            print "2. Koefisien "
            print "  yaitu suatu bilangan yang menyetai variabel"
            print "3. Konstanta"
            print "  yaitu bagian dari bentuk aljabar yang tidak memuat variabel"
            print "4. Suku"
            print "  yaitu bagian dari bentuk aljabar yang berupa variabel "
            print "  beserta koefisien/konstant yang dipisahkan - atau +"
elif pilih == "3":
    print ""
    print "WA = +62852 1707 8508"
    print "INSTAGRAM = @raghibhabibi"
elif pilih == "4":

    print ""
    def print_faktor(x):
        print "faktor dari", x, "adalah = "
        for i in range(1, x+1):
            if x % i == 0:
                print(i)
    num = int(input("masukkan bilangan = "))

    print_faktor(num)
else:
    print "input salah, harap coba lagi"
    

      
            
        
            
        
            


                
