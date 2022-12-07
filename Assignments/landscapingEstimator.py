class LandscapingEstimator:
    # Yard Cutting Properties
    YardArea = 0
    YardCuttingRate = 0 #charge per sqft
    YardLength = 0
    YardWidth = 0

    # Weed Eating
    LinearFeet = 0
    WeedEatingRate = 0
    YardLength = 0
    YardWidth = 0

    #Lighting
    LightCost = 0 #Light Cost + Rate/Light
    QuantityLights = 0

    def __init__(this, yardCuttingRate, weedEatingRate, lightingCost):
        this.YardCuttingRate = yardCuttingRate
        this.WeedEatingRate = weedEatingRate
        this.LightCost = lightingCost

    def GetYardCuttingCost(this, area = 0, length = 0, width = 0):
        if area > 0:
            cost = area * this.YardCuttingRate
            return cost
        if area <= 0:
            calculatedArea = length * width
            cost = calculatedArea * this.YardCuttingRate
            return cost
    
    def GetWeedCuttingCost(this, length = 0, width = 0):
        calculatedPerimeter = (length * 2) + (width * 2)
        cost = calculatedPerimeter * this.WeedEatingRate
        return cost
    
    def GetLightingInstallationCost(this, lights):
        return lights * this.LightCost



leosEstimator = LandscapingEstimator(0.02, 2, 45)
yardEstimate = leosEstimator.GetYardCuttingCost(0, 96, 40)
weedTrimmingEstimate = leosEstimator.GetWeedCuttingCost(96, 40)
lightingEstimate = leosEstimator.GetLightingInstallationCost(17)


print(yardEstimate)
print(weedTrimmingEstimate)
print(lightingEstimate)
yardTotal = yardEstimate + weedTrimmingEstimate + lightingEstimate

print(yardTotal)

donaldsEstimator = LandscapingEstimator(0.80, 3, 65)

