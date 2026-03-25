from Tempreture.celsius import c_to_f , c_to_k
from Tempreture.fahrenheit import f_to_c
from Tempreture.kelvin import k_to_c


def main():
    print("Temperatrue conversion options :")
    print("1. Celsius to Fahrenheit ")
    print("2. Fahrenheit to Celsiys ")
    print("3. Celsius to Kelvin ")

    choice = int(input("Enter your choice (1/2/3) :"))

    if choice == 1 :
        celsius = float(input("Enter temperature in Celsius:"))
        print(f"{celsius}℃ = {c_to_f (celsius)}℉")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in fahrenheit"))
        print(f"{fahrenheit}℉ = {f_to_c (fahrenheit)}℃")

    elif choice == 3:
        kelvin = float(input("Enter tempreture in kelvin :"))
        print(f"{kelvin} = {k_to_c(kelvin)}")

    else:
        print("Invalid choice ")

main()