import pandas as pd
from ReadFile import readExcel
from Fuzzyfication import fuzzify_service, fuzzify_price
from FuzzyRules import applyRules
from Defuzzification import defuzzify, get_category

# Inisialisasi list hasil
services_fuzzy = []
prices_fuzzy   = []
scores         = []
categories     = []

def main():
    # Baca data dari file Excel
    df = readExcel()

    for index, row in df.iterrows():
        # Fuzzifikasi input
        service_fuzzy = fuzzify_service(row['Pelayanan'])  # sesuai Excel
        price_fuzzy   = fuzzify_price(row['harga'])        # sesuai Excel

        services_fuzzy.append(service_fuzzy)
        prices_fuzzy.append(price_fuzzy)

        # Inferensi (apply fuzzy rules)
        rules_fired = applyRules(prices_fuzzy[index], services_fuzzy[index])

        # Defuzzifikasi -> score crisp
        score    = defuzzify(rules_fired)
        category = get_category(score)

        scores.append(score)
        categories.append(category)

    # Masukin ke DataFrame
    df['Score']       = scores
    df['Rekomendasi'] = categories

    # Ambil 5 restoran terbaik berdasarkan score tertinggi
    top5 = df.nlargest(5, 'Score')[['id Pelanggan', 'Pelayanan', 'harga', 'Score', 'Rekomendasi']]
    top5 = top5.reset_index(drop=True)
    top5.index += 1  # ranking mulai dari 1

    # Tampilkan hasil di console
    print("=== 5 Restoran Terbaik ===")
    print(top5.to_string())

    # Simpan ke file peringkat.xlsx
    output_path = 'peringkat.xlsx'
    top5.to_excel(output_path, index=True, index_label='Peringkat')
    print(f"\nHasil disimpan ke: {output_path}")


if __name__ == "__main__":
    main()