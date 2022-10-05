
# Online Python - IDE, Editor, Compiler, Interpreter
jalan = True
while (jalan==True):
    r = float(input("Masukan Jari-jari : "))
    luas = 22/7*(r*r)
    keliling = 2*22/7*r
    print ("Luas Lingkaran \t\t= ",luas)
    
    l=input("apakah ingin keluar tanpa menghitung keliling? (y=1/n=2) : ")
    if (l=='1'):
        print ("Keliling Lingkaran\t= ",keliling)
    else:
        print ("terimakasih")
    break
