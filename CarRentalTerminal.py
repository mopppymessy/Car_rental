1#Car rental terminal

1 == "Car Rental"
2 == "Car Return"
3 == "Print the totals"


from tabulate import tabulate

car = [1, 2, 3]
rent_costs = [90, 60, 40]
insurance = [25, 40, 35]
tax_ = 0.05
available=[6,2,4]

data = [[1,"Camry",6,"90QR", "25QR", "50QR"], 
            [2,"Pajero",2, "60QR", "40QR", "60QR" ], 
            [3,"Altima",4, "40QR", "35QR", "70QR" ]]
   


def main():
    while True:
        option= input("Please select one: \n1. Car Rental \n2. Car Return \n3. Print the totals \noption no.: ")
        if option=='1':
            print("Select one of the available cars")
            def car_rent():
                data = [[1,"Camry",6,"90PKR", "20PKR", "50PKR"], 
                        [2,"Pajero",2, "60PKR", "20PKR", "60PKR" ], 
                        [3,"Altima",4, "40PKR", "30PKR", "70PKR" ]]
                
                #headings names
                col_names = ["no.","car", "Available", "Price/day", "Liabilty insurance/day", "Full insurance/day"]
                
                #table with tabulate function
                print(tabulate(data, headers=col_names))
                print("-"*87)
                while True:
                    user_input = int(input("Enter Car Type: "))
                    if user_input == 1:
                        if data[user_input-1][2] == 0:
                            print("Car is unavailable, pick another car.")
                            continue
                        data[user_input-1][2] = data[user_input-1][2]-1
                        days = input("Enter the number of days: ")
                        days = int(days)
                        if days <= 0:
                            print("Invalid number of days")
                            continue
                        insurance_in = input("Enter 'L' for liability, 'F' for full insurance(L, F): ")
                        insurance = insurance_in.upper()
                        #liability insurance is taken

                        if insurance=="l" or insurance=="L":
                            insurance_cost=days*25
                            rent=days*rent_costs[1]                            
                            Tax=rent*tax_
                            totalins=rent+insurance_cost+Tax
                            print("-"*87)
                            print("Rent Cost: QR ", + rent)
                            print("Insurance Cost: QR",+ insurance_cost)
                            print("Tax ('5%' on Rental): QR ", + Tax)
                            print("-"*87)
                            print("Total: QR ", + totalins)
                            print("-"*87)
                            
                            break
                        #full insurance is taken
                        elif insurance=="f" or insurance=="F":
                            insurance_cost=days*50
                            rent=days*rent_costs[1]                            
                            Tax=rent*tax_
                            totalins=rent+insurance_cost+Tax
                            print("-"*87)
                            print("Rent Cost: QR ", + rent)
                            print("Insurance Cost: QR",+ insurance_cost)
                            print("Tax ('5%' on Rental): QR ", + Tax)
                            print("-"*87)
                            print("Total: QR ", + totalins)
                            print("-"*87)

                            break
                        else:
                            insurance != "L" or insurance != "F" or insurance != "l" or insurance != "f"
                            print("Invalid insurance type")
                            continue
                    if user_input == 2:
                        days = input("Enter the number of days: ")
                        days = int(days)
                        if days <= 0:
                            print("Invalid number of days")
                            continue
                        insurance_in = input("Enter 'L' for liability, 'F' for full insurance(L, F): ")
                        insurance = insurance_in.upper()
                        if insurance=="l" or insurance=="L":
                            insurance_cost=days*40
                            rent=days*rent_costs[1]                            
                            Tax=rent*tax_
                            totalins=rent+insurance_cost+Tax
                            print("-"*87)
                            print("Rent Cost: QR ", + rent)
                            print("Insurance Cost: QR",+ insurance_cost)
                            print("Tax ('5%' on Rental): QR ", + Tax)
                            print("-"*87)
                            print("Total: QR ", + totalins)
                            print("-"*87)

                            break
                        elif insurance=="f" or insurance=="F":
                            insurance_cost=days*60
                            rent=days*rent_costs[1]                            
                            Tax=rent*tax_
                            totalins=rent+insurance_cost+Tax
                            print("-"*87)
                            print("Rent Cost: QR ", + rent)
                            print("Insurance Cost: QR",+ insurance_cost)
                            print("Tax ('5%' on Rental): QR ", + Tax)
                            print("-"*87)
                            print("Total: QR ", + totalins)
                            print("-"*87)

                            break
                        else:
                            insurance != "L" or insurance != "F" or insurance != "l" or insurance != "f"
                            print("Invalid insurance type")
                            continue
                    if user_input == 3:
                        days = input("Enter the number of days: ")
                        days = int(days)
                        if days <= 0:
                            print("Invalid number of days")
                            continue
                        insurance_in = input("Enter 'L' for liability, 'F' for full insurance(L, F): ")
                        insurance = insurance_in.upper()
                        if insurance=="l" or insurance=="L":
                            insurance_cost=days*35
                            rent=days*rent_costs[1]                            
                            Tax=rent*tax_
                            totalins=rent+insurance_cost+Tax
                            print("-"*87)
                            print("Rent Cost: QR ", + rent)
                            print("Insurance Cost: QR",+ insurance_cost)
                            print("Tax ('5%' on Rental): QR ", + Tax)
                            print("-"*87)
                            print("Total: QR ", + totalins)
                            print("-"*87)
                            break
                        elif insurance=="f" or insurance=="F":
                            insurance_cost=days*75
                            rent=days*rent_costs[1]                            
                            Tax=rent*tax_
                            totalins=rent+insurance_cost+Tax
                            print("-"*87)
                            print("Rent Cost: QR ", + rent)
                            print("Insurance Cost: QR",+ insurance_cost)
                            print("Tax ('5%' on Rental): QR ", + Tax)
                            print("-"*87)
                            print("Total: QR ", + totalins)
                            print("-"*87)

                            break
                        else:
                            insurance != "L" or insurance != "F" or insurance != "l" or insurance != "f"
                            print("Invalid insurance type")
                            continue
            car_rent()

            while True:
                        nex_t = input("More operations? [Y/N]: ")
                        nex_t = nex_t.upper()
                        if nex_t == "N":
                            break
                        elif nex_t=="Y":
                            main()
                        else:
                            print("Invalid Input")

        elif option=='2':     
            def car_return(car):
                print(input("Select the type of car that needs to be returned: "))
                for i in range(len(data)):
                    if car==data[i][0]:
                        data[i][0]+=1
                        break
                print("Car returned!")        
            car_return(car)
        #if user wants further operations
            while True:
                        nex_t = input("More operations? [Y/N]: ")
                        nex_t = nex_t.upper()
                        if nex_t == "N":
                            break
                        elif nex_t=="Y":
                            main()
                        else:
                            print("Invalid Input")
        elif option=='3':
            def print_out():
                    Total_income =rent_costs[1] * insurance[0]
                    Total_insurance = insurance[1]*rent_costs[2]
                    Total_tax = tax_*insurance[2]
                    print("Total Income:  QR ", + Total_income)
                    print("Total Insurance:  QR ", + Total_insurance)
                    print("Total Tax:  QR ", + Total_tax)
            print_out()
#if user wants to further operations
            while True:
                        nex_t = input("More operations? [Y/N]: ")
                        nex_t = nex_t.upper()
                        if nex_t == "N":
                            break
                        elif nex_t=="Y":
                            main()
                        else:
                            print("Invalid Input")            
        else:
            option!='1' or option!='2' or option!='3'
            print("Invalid input, Please select Option 1 , 2 or 3 only.")

main()

    