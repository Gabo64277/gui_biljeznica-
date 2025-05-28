import tkinter as tk

def spremi_poruku():
    tekst = unos.get()
    if tekst:
        with open("poruke.txt", "a") as dat:
            dat.write(tekst + "\n")
        unos.delete(0, tk.END)
        info_label.config(text="Poruka je dodana u arhivu.", fg="green")
    else:
        info_label.config(text="Molimo unesite poruku prije spremanja.", fg="red")

def prikazi_poruke():
    try:
        with open("poruke.txt", "r") as dat:
            svi_redovi = dat.read()
            if svi_redovi.strip():
                prikaz_label.config(text=svi_redovi)
            else:
                prikaz_label.config(text="Arhiva je trenutno prazna.")
    except FileNotFoundError:
        prikaz_label.config(text="Nema dostupne arhive poruka.")

def izlaz():
    korijenski.destroy()

def pokreni_sucelje():
    global unos, prikaz_label, info_label, korijenski

    korijenski = tk.Tk()
    korijenski.title("Moja Arhiva Poruka")

    naslov = tk.Label(korijenski, text="Upišite novu poruku:")
    naslov.pack(pady=10)

    unos = tk.Entry(korijenski, width=45)
    unos.pack(pady=10)

    gumb_spremi = tk.Button(korijenski, text="Spremi Poruku", command=spremi_poruku)
    gumb_spremi.pack()

    gumb_prikazi = tk.Button(korijenski, text="Prikaži Sve Poruke", command=prikazi_poruke)
    gumb_prikazi.pack(pady=10)

    info_label = tk.Label(korijenski, text="", fg="green")
    info_label.pack(pady=5)

    prikaz_label = tk.Label(korijenski, text="", justify="left", anchor="nw")
    prikaz_label.pack(pady=10)


    gumb_izlaz = tk.Button(korijenski, text="Izlaz", command=izlaz, fg="white", bg="red")
    gumb_izlaz.pack(pady=10)

    korijenski.mainloop()

pokreni_sucelje()
