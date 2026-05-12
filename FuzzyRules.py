from numpy import double

badExist = bool
avgExist = bool
goodExist = bool

cheapExist = bool
expensiveExist = bool

def checkExistence(price, quality):
    global badExist, avgExist, goodExist, cheapExist, expensiveExist
    badExist = quality[0] > 0.0
    avgExist = quality[1] > 0.0
    goodExist = quality[2] > 0.0
    cheapExist = price[0] > 0.0
    expensiveExist = price[1] > 0.0

def applyRules(price, quality) -> list[double]:
    checkExistence(price, quality)
    
    recommend = 0.0
    notRecommend = 0.0

    # Rule 1: Bad & Cheap = Not Recommended
    if badExist and cheapExist:
        val = min(quality[0], price[0])
        notRecommend = max(notRecommend, val)

    # Rule 2: Bad & Expensive = Not Recommended
    if badExist and expensiveExist:
        val = min(quality[0], price[1])
        notRecommend = max(notRecommend, val)

    # Rule 3: Avg & Cheap = Recommended
    if avgExist and cheapExist:
        val = min(quality[1], price[0])
        recommend = max(recommend, val)

    # Rule 4: Avg & Expensive = Not Recommended
    if avgExist and expensiveExist:
        val = min(quality[1], price[1])
        notRecommend = max(notRecommend, val)

    # Rule 5: Good & Cheap = Recommended
    if goodExist and cheapExist:
        val = min(quality[2], price[0])
        recommend = max(recommend, val)

    # Rule 6: Good & Expensive = Recommended
    if goodExist and expensiveExist:
        val = min(quality[2], price[1])
        recommend = max(recommend, val)

    return [recommend, notRecommend]    