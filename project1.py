#arrays to store data
prompts = ["Please enter the total minutes you spend showering in a week (time per shower * number of showers):",
          "Please enter the number of meals you eat per week:",
          "Please enter the number of miles driven in a week:"]
inputs = []
const = [2, 2.5, .404]
units = ["gallons", "kg CO₂eq", "kg CO₂eq"]
impact = []


#asks user for values
for i in range(len(prompts)):
    inputs.append(int(input(prompts[i])))        


#calculation(individual and total)
for i in range(len(inputs)):
    impact.append(round(inputs[i] * const[i], 2))

total_impact = 0
for i in range(len(impact)):
    total_impact += impact[i]


#final report
print("Your weekly enviornmental impact results are: ")
for i in range(len(inputs)):
    print(str(impact[i]), units[i])

print("Your total impact is:", round(total_impact, 2), "kg CO₂eq this week.")






'''
#1
showers = int(input("Please enter the number of showers you take per week:"))
time = int(input("Please enter how long your average showers are in minutes:"))

total_length = showers * time
print("So your total weekly shower time is", str(total_length), "minutes.")

#1.2
meals = int(input("Please enter the number of meals you eat per week:"))

#1.3
miles = int(input("Please enter the number of miles driven in a week:"))

water_const = 2 #5*2 = 10?
meals_const = 2.5 #kg CO₂eq per meal from Chatgpt
miles_const = .404 #kg CO₂eq per mile from Chatgpt

avg_water = water_const * total_length
meals_impact = meals_const * int(meals)
miles_impact = miles_const * int(miles)

print("Your water consumption is", avg_water, "gallons in a week.")
print("Your enviornmental impact based on the number of meals you eat per week is " + str(meals_impact) + "kg CO₂eq.")

'''