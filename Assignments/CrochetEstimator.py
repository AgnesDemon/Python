class Crochet:
    Yarn = 0
    CrochetTools = 0
    Eyes = 0
    Pattern = 0

    Hours = 0

    def __init__(this, yarn, tools, eyes, pattern, hours):
        this.Yarn = yarn
        this.CrochetTools = tools
        this.Eyes = eyes
        this.Pattern = pattern
        this.Hours = hours
    
    def SupplyCost(this):
        cost = this.Yarn + this.CrochetTools + this.Eyes + this.Pattern
        return cost
    
    def HourlyCost(this):
        hourcost = this.Hours * 12
        return hourcost
    

crochetBag = Crochet(5, 30, 1, 0, 8)
hourlyCost = crochetBag.HourlyCost()
supplyCost = crochetBag.SupplyCost()
totalCost1 = hourlyCost + supplyCost
#total = crochetBag.HourlyCost + crochetBag.SupplyCost()

print("Bag:", totalCost1)
#print(hourlyCost)
#print(supplyCost)
#print(hourlyCost + supplyCost)

crochetSchnauzer = Crochet(4, 30, 1, 6, 7)
hourlyCost = crochetSchnauzer.HourlyCost()
supplyCost = crochetSchnauzer.SupplyCost()
totalCost2 = hourlyCost + supplyCost

print("Schnauzer:", totalCost2)
#print(hourlyCost)
#print(supplyCost)
#print(hourlyCost + supplyCost)

print()
print("Total Earnings:", totalCost1 + totalCost2)
