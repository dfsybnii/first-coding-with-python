def sapa():
    print(f"Halo, {nama}!")




print("Welcome, World")


nama = input(" Siapa nama lu? ").strip().title().capitalize()


sapa()


nilai = 50 

def ubah_nilai():

  global nilai

nilai = 100
print(f"Nilai {nama}: {nilai} ")

ubah_nilai()
