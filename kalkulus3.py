def hitung_f(x=0):
    return 2 * x**2 - 3 * x + 1

x = int(input("Masukan x (default=0): ") or 0)
hasil = hitung_f(x)
print("Hasil: ", hasil)