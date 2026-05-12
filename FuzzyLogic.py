from numpy import double
from ReadFile import readExcel
from Fuzzyfication import fuzzify_service, fuzzify_price
from FuzzyRules import applyRules

services_fuzzy = list[double]
prices_fuzzy = list[double]
recommend_fuzzy = list[double]

def main():
    df = readExcel()
    
    for index, row in df.iterrows():
        services_fuzzy.append(fuzzify_service(row['service']))
        prices_fuzzy.append(fuzzify_price(row['price']))
        recommend_fuzzy.append(applyRules(prices_fuzzy[index], services_fuzzy[index]))

if __name__ == "__main__":
    main()
