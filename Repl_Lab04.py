nama = input('Masukkan Nama: ')
i = 0
while i <= len(nama):
  print(nama[0:i])
  i += 1
print("\n")

while True:
  teks = input("Masukkan teks: ")
  if len(teks) >= 8 and (teks.endswith("yyy") or teks.endswith("YYY")) and (teks.count("nf") or teks.count("NF") or teks.count("Nf") or teks.count("nF")) and not teks.isalpha():
    print("Teks valid. Program berhenti")
    break
  else:
    print("Teks tidak valid")