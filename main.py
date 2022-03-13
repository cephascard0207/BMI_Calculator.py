#BMI CALCULATOR
#BODY-MASS-INDEX
#Created by Cephas Cardozo, 12/03/2022

print("BMI CALCULATOR")
print("v1.0\n")

height = input("Enter your height in metres: ")
weight = input("Enter your weight in  kilograms: ")

#'r' stands for result
#We have converted Strings into Float here to be able to mathematically calculate and find the BMI

r_height = float(height)
r_weight = float(weight)

bmi = r_weight / (r_height * r_height)

print(bmi)