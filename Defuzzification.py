from numpy import double


def defuzzify(rules_fired: list[tuple]) -> double:
   
    # Jika tidak ada rule yang aktif, return 0
    if not rules_fired:
        return 0.0

    numerator   = sum(alpha * z for alpha, z in rules_fired)
    denominator = sum(alpha     for alpha, _ in rules_fired)

    if denominator == 0:
        return 0.0

    return numerator / denominator


def get_category(score: double) -> str:
   
    if score <= 40:
        return "rendah"
    elif score <= 70:
        return "sedang"
    else:
        return "tinggi"