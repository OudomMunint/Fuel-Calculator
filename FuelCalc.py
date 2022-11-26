#Dev: Dom, L1 SWE
#Displays the previous Km reading, current kKm reaing, price per liter of fuel, cost of fuel.
#Calculates the Km travelled, Number of litres used and fuel consumed.


#Parameters
def consumption(previousKm, currentKm, priceFuel, totalCost):
#Calculations pulled from previous ()
   kmTravelled = currentKm - previousKm
   litres = (totalCost / priceFuel) * 100
   fuelConsumption = (litres / kmTravelled) *100
   #Displays lines for decoration
   print("=========================================")
   
   #Displays the last Km reading + it's value
   print("  Last kilometre reading = " + str(previousKm) + " kms")
   
   #Displays the current Km reading + it's value
   print("  Current kilometre reading = " + str(currentKm) + " kms")
   
   #Displays the Price/Litre + it's value
   print("  price per litre = " + str(priceFuel) + " Cent/Litres ")
   
   #Displays the Fuel bought + it's value
   print("  Fuel purchased cost = " + "$" + str(totalCost))
   
   #Displays lines for decoration
   print("=========================================")
   
   #Displays Km travelled + it's value
   print("  Kilometres travelled = " + str(kmTravelled) + " kms")
   
   #Displays litres consumed + it's value
   print("  Number of litres = " + str(litres) + " litres")
   
   #Displays Fuel consumed in Litre/100Km + it's value
   print("  Fuel comsumed = " + str(totalCost)+ " Litres/100Km")
   
   
#Calculates and prints the fuel consumption in liters per 100km   
def displayConsumption(previousKm, currentKm, priceFuel, totalCost):

#Calculations
   kmTravelled = currentKm - previousKm
   litres = (totalCost / priceFuel) * 100
   fuelConsumption = (litres / kmTravelled) *100
   
#Decoration and displays Km travelled, Liters, fuel comsumed + it's values   
   print("=========================================")
   print("  Kilometres travelled = " + str(kmTravelled) + " kms")
   print("  Number of litres = " + str(litres) + " litres")
   print("  Fuel comsumed = " + str(totalCost)+ " Litres/100Km")
   
   
   
