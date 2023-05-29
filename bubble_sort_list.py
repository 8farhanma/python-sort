def bubble_sort(angka):
    n = len(angka)
    for i in range(n-1):
        for j in range(n-i-1):
            if angka[j] < angka[j+1]:
                angka[j], angka[j+1] = angka[j+1], angka[j]

#Daftar angka
angka = [42, 19, 33, 8, 55]

# Memanggil fungsi bubble_sort untuk mengurutkan daftar angka
bubble_sort(angka)

# Mencetak daftar nilai yang telah diurutkan
print("Hasil pengurutan secara descending : ", angka)