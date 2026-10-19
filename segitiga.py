# Meminta masukan bilangan bulat N dari pengguna
N = int(input("Masukkan bilangan bulat (1 - 100): "))

# Perulangan (looping) untuk menggambar segitiga siku-siku
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print()