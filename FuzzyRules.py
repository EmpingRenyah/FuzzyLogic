def applyRules(price, quality) -> list:
    cheap, expensive = price
    bad, avg, good   = quality

    recommend    = 0.0
    notRecommend = 0.0

    # Rule 1: Bad & Cheap → Not Recommended
    alpha = min(quality[0], price[0])
    if alpha > 0:
        notRecommend = max(notRecommend, alpha)

    # Rule 2: Bad & Expensive → Not Recommended
    alpha = min(quality[0], price[1])
    if alpha > 0:
        notRecommend = max(notRecommend, alpha)

    # Rule 3: Avg & Cheap → Recommended
    alpha = min(quality[1], price[0])
    if alpha > 0:
        recommend = max(recommend, alpha)

    # Rule 4: Avg & Expensive → Not Recommended
    alpha = min(quality[1], price[1])
    if alpha > 0:
        notRecommend = max(notRecommend, alpha)

    # Rule 5: Good & Cheap → Recommended
    alpha = min(quality[2], price[0])
    if alpha > 0:
        recommend = max(recommend, alpha)

    # Rule 6: Good & Expensive → Recommended
    alpha = min(quality[2], price[1])
    if alpha > 0:
        recommend = max(recommend, alpha)

    return [recommend, notRecommend]