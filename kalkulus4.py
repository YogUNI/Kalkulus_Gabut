def hitung_f(x):
    try:
        return 2 * x**2 - 3 * x + 1
    except TypeError:
        return "Input harus berupa angka"

x = input("Masukan x: ")
try:
    x = int(x)
    hasil = hitung_f(x)
    print("Hasil: ", hasil)
except ValueError:
    print("Input harus berupa angka")