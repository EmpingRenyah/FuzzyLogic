import pandas as pd
from ReadFile import readExcel
from Fuzzyfication import fuzzify_service, fuzzify_price
from FuzzyRules import applyRules
from Defuzzification import defuzzify

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

        # Inferensi
        recommendation = applyRules(price_fuzzy, service_fuzzy)

        # Defuzzifikasi
        score = defuzzify(recommendation)
        scores.append(score)
        
    #simpan ke dataframe
    df['Score'] = scores

    top5 = df.nlargest(5, columns=['Score', 'Pelayanan'])[['id Pelanggan', 'Pelayanan', 'harga', 'Score']]
    top5 = top5.reset_index(drop=True)
    top5.index += 1

    print("=== 5 Restoran Terbaik ===")
    print(top5.to_string())

    output_path = 'peringkat.xlsx'
    top5.to_excel(output_path, index=True, index_label='Peringkat')
    print(f"\nHasil disimpan ke: {output_path}")


if __name__ == "__main__":
    main()