from random import randint
#loop 25 times
#write information and put enter at the end

randomBillNumber = randint(50,1000)

print("phone: ", ",", randomBillNumber)

names = ["Denji", "Aki", "Power", "Angel", "Makima", 
    "Pochita", "Himeno", "Kobeni", "Meowy", "Hirokazu", 
    "Sawatari", "Beam", "Reze", "Violence", "Dororo",
    "Midoriya", "Bakugo", "Ochaco", "All Might", "Yoh",
    "Hao", "Ren", "Opacho", "Anna", "Kishibe"]
#print(names)
for name in names:
    print(name)

#row = 25
#while row < 25:
    #print(name, ",", randomBillNumber)

#phoneBill = randomBillNumber
#electricBill = randomBillNumber
#print(phoneBill)
#print(electricBill)

randomPhoneBill = randint(100, 500)
randomHouseBill = randint(100, 1000)
randomElectricBill = randint(100, 500)
randomWaterBill = randint(50, 200)
randomFoodBill = randint(100, 400)
#print(randomPhoneBill)
#print(randomHouseBill)
#print(randomElectricBill)
#print(randomWaterBill)
#print(randomFoodBill)

#print(name, ",", randomPhoneBill, ",", randomHouseBill, ",", randomElectricBill, ",", randomWaterBill, ",", randomFoodBill)
def Bills():
    print(name, ",", randomPhoneBill, ",", randomHouseBill, ",", randomElectricBill, ",", randomWaterBill, ",", randomFoodBill)

Bills()


