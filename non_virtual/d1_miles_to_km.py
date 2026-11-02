#constants
MILES_TO_KM = 8 / 5
KM_TO_MILES = 5 / 8

#user input
miles = 20
km = 19

#logic 
convert_miles_to_km = miles * MILES_TO_KM
convert_km_to_miles =  km * KM_TO_MILES

# Display 
print(f"{miles} miles → {convert_miles_to_km: .2f} km")
print(f"{km} km → {convert_km_to_miles: .3f} miles")