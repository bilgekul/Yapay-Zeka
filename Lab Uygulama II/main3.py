favori_meyveler = ["elma", "armut", "çilek", "vişne", "muz"]

ornek_meyveler = ["elma", "armut", "karpuz", "kavun", "muz", "portakal", "çilek", "vişne", "kiraz", "mandalina"]

for meyve in ornek_meyveler:
    if meyve in favori_meyveler:
        print(f"{meyve} favori meyvelerinizde bulunuyor.")
    else:
        print(f"{meyve} favori meyvelerinizde bulunmuyor.")
