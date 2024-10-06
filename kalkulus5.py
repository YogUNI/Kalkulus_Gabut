def decorator_f(f):
    def wrapper(x):
        return f(x)
    return wrapper

@decorator_f
def hitung_f(x):
    return 2 * x**2 - 3 * x + 1

x = int(input("Masukan x: "))
hasil = hitung_f(x)
print("Hasil: ", hasil)