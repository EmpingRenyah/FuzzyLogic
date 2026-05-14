from numpy import double

# Nilai crisp output untuk tiap kategori rekomendasi
SCORE_RENDAH = 30   # tidak direkomendasikan
SCORE_SEDANG = 60   # so so
SCORE_TINGGI = 90   # sangat direkomendasikan


def applyRules(price, quality) -> list[tuple]:
    cheap,     expensive = price
    bad,  avg, good      = quality

    rules_fired = []

    # Rule 1: Bad & Cheap = Not Recommended
    alpha = min(quality[0], price[0])
    if alpha > 0:
        rules_fired.append((alpha, SCORE_RENDAH))

    # Rule 2: Bad & Expensive = Not Recommended
    alpha = min(quality[0], price[1])
    if alpha > 0:
        rules_fired.append((alpha, SCORE_RENDAH))

    # Rule 3: Avg & Cheap = Recommended
    alpha = min(quality[1], price[0])
    if alpha > 0:
        rules_fired.append((alpha, SCORE_SEDANG))

    # Rule 4: Avg & Expensive = Not Recommended
    alpha = min(quality[1], price[1])
    if alpha > 0:
        rules_fired.append((alpha, SCORE_RENDAH))

    # Rule 5: Good & Cheap = Recommended
    alpha = min(quality[2], price[0])
    if alpha > 0:
        rules_fired.append((alpha, SCORE_TINGGI))

    # Rule 6: Good & Expensive = Recommended
    alpha = min(quality[2], price[1])
    if alpha > 0:
        rules_fired.append((alpha, SCORE_SEDANG))

    return rules_fired