import numpy as np

def centroid_defuzzification(universe, membership_values):
    numerator   = np.sum(universe * membership_values)
    denominator = np.sum(membership_values)

    if denominator == 0:
        return np.mean(universe)

    return numerator / denominator


def defuzzify(recommendation: list) -> float:
    # universe = [0, 1] → index 0 = notRecommend, index 1 = recommend
    universe          = np.array([0, 1])
    membership_values = np.array(recommendation)  # [recommend, notRecommend]

    return centroid_defuzzification(universe, membership_values)