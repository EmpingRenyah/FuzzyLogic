from typing import Final

SERVICE_BAD:  Final = [0,  30, 40]
SERVICE_AVG:  Final = [30, 40, 60, 70]
SERVICE_GOOD: Final = [60, 70, 100]

PRICE_CHEAP:     Final = [20000, 35000, 45000]
PRICE_EXPENSIVE: Final = [30000, 40000, 60000]


def fuzzify_service(service: int) -> list[float]:
    bad  = 0.0
    avg  = 0.0
    good = 0.0

    # check for pure bad (service <= 30)
    if service <= SERVICE_BAD[1]:
        bad = 1.0
    # check for pure good (service >= 70)
    elif service >= SERVICE_GOOD[1]:
        good = 1.0
    # check for pure average (service 40-60)
    elif service >= SERVICE_BAD[2] and service <= SERVICE_AVG[2]:
        avg = 1.0

    # transisi bad -> avg (service 30-40)
    if service > SERVICE_BAD[1] and service < SERVICE_BAD[2]:
        bad = (SERVICE_BAD[2] - service) / (SERVICE_BAD[2] - SERVICE_BAD[1])
        avg = (service - SERVICE_AVG[0]) / (SERVICE_AVG[1] - SERVICE_AVG[0])

    # transisi avg -> good (service 60-70)
    if service > SERVICE_AVG[2] and service < SERVICE_GOOD[1]:
        avg  = (SERVICE_AVG[3] - service) / (SERVICE_AVG[3] - SERVICE_AVG[2])
        good = (service - SERVICE_GOOD[0]) / (SERVICE_GOOD[1] - SERVICE_GOOD[0])

    return [bad, avg, good]


def fuzzify_price(price: int) -> list[float]:
    cheap     = 0.0
    expensive = 0.0

    # Logic for the "Cheap" line 
    if price <= PRICE_CHEAP[1]:
        cheap = 1.0
    elif PRICE_CHEAP[1] < price <= PRICE_CHEAP[2]:
        # Linear decrease: (x2 - x) / (x2 - x1)
        cheap = (PRICE_CHEAP[2] - price) / (PRICE_CHEAP[2] - PRICE_CHEAP[1])
    else:
        cheap = 0.0

    # Logic for the "Expensive" line
    if price <= PRICE_EXPENSIVE[0]:
        expensive = 0.0
    elif PRICE_EXPENSIVE[0] < price <= PRICE_EXPENSIVE[1]:
        # Linear increase: (x - x1) / (x2 - x1)
        expensive = (price - PRICE_EXPENSIVE[0]) / (PRICE_EXPENSIVE[1] - PRICE_EXPENSIVE[0])
    else:
        expensive = 1.0

    return [cheap, expensive]