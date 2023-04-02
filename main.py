# QAP 4, Jacob Jesso
# Program for The One Stop Insurance Company

import datetime
from datetime import timedelta
import FormatValues as FV

# Open OSICDef.dat file and read the Values into Variables

f = open("OSICDef.dat.py", "r")
POLICY_NUM = int(f.readline())
BASE_RATE = float(f.readline())
ADD_DISC_RATE = float(f.readline())
ADD_LIB_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOAN_CAR_RATE = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()

# Inputs for the Program

while True:
    CusFirstName = input("Enter the Customers First Name: ").title()
    CusLastName = input("Enter the Customers Last Name: ").title()
    CusAddress = input("Enter the Customers Address: ").title()
    City = input("Enter the Customers City: ").title()
    Prov = input("Enter the Customers Province: ").title()
    Postal = input("Enter the Customers Postal Code (X1X 1X1): ").upper()
    PhoneNum = input("Enter the Customers Phone Number (xxx-xxx-xxxx): ")
    NumCars = int(input("Enter the Number of cars being insured: "))
    ExtraLiability = input("Enter whether the Customer wants extra liability (Y or N): ").upper()
    OptLoanCar = input("Enter whether optional loaner car (Y or N): ").upper()
    OptGlassCov = input("Enter whether the Customer would like additional coverage for glass (Y or N): ").upper()
    PayOption = input("Enter whether Customer will pay in full or monthly (F or M): ").upper()
    PolicyStartDate = datetime.datetime.now()
    PolicyStartDateDsp = PolicyStartDate.strftime("%Y-%m-%d")

# Calculations needed for the Program

    if NumCars == 1:
        BaseCost = BASE_RATE
    else:
        BaseCost = BASE_RATE * NumCars - (((NumCars - 1) * BASE_RATE) * ADD_DISC_RATE)

    if ExtraLiability == "Y":
        ExtraLiabilityCost = ADD_LIB_RATE * NumCars
    elif ExtraLiability == "N":
        ExtraLiabilityCost = 0
    else:
        break

    if OptGlassCov == "Y":
        OptGlassCost = GLASS_COV_RATE * NumCars
    elif OptGlassCov == "N":
        OptGlassCost = 0
    else:
        break

    if OptLoanCar == "Y":
        OptLoanCost = LOAN_CAR_RATE * NumCars
    elif OptLoanCar == "N":
        OptLoanCost = 0
    else:
        break

    ExtraCost = ExtraLiabilityCost + OptLoanCost + OptGlassCost
    TotInsurePrem = ExtraCost + BaseCost
    HST = TotInsurePrem * HST_RATE
    TotFullCost = TotInsurePrem + HST

    if PayOption == "M":
        MonPayment = (TotFullCost + PROCESS_FEE) / 8
    else:
        MonPayment = 0

    if PolicyStartDateDsp > "25":
        PolicyStartDateDsp = ((PolicyStartDate.replace(day=1) + timedelta(days=32)).replace(day=1))

    # Print Statement

    print("-"*43)
    print("One Stop Insurance Company Invoice")
    print()
    print(f"{POLICY_NUM}-{CusFirstName[0]}{CusLastName[0]} ")
    print(f"{CusAddress:<20}, {City:<10}, {Prov:<10}")
    print(f"{Postal:<6},      {PhoneNum:<10}")
    print(f"Policy Start Date:              {(PolicyStartDateDsp)}")
    print("-"*43)
    print(f"Number of Vehicles on Policy:         {NumCars}")
    print()
    print(f"Cost of Extra Liability:          {FV.FDollar2(ExtraLiabilityCost)}")
    print(f"Cost of Loaner car option:        {FV.FDollar2(OptLoanCost)}")
    print(f"Cost of Optional glass coverage:  {FV.FDollar2(OptGlassCost)}")
    print("                                  ---------")
    print(f"Total Cost of Extra Coverage:     {FV.FDollar2(ExtraLiabilityCost)}")
    print(f"Cost of Base Policy:              {FV.FDollar2(BaseCost)}")
    print(f"Total Premium Cost:               {FV.FDollar2(TotInsurePrem)}")
    print(f"HST:                              {FV.FDollar2(HST)}")
    print("                                  ---------")
    print(f"Total Cost Plus HST (@15%)        {FV.FDollar2(TotFullCost)}")
    if PayOption == "M":
        print(f"Monthy Payment                    {FV.FDollar2(MonPayment)}")
    else:
        break

    # Open Policies.dat file and read the Values and Variables

    f = open("Policies.dat.py", "a") as a:
    f.write("{}, ".format(int(POLICY_NUM)))
    f.write("{}, ".format(CusFirstName))
    f.write("{}, ".format(CusLastName))
    f.write("{}, ".format(CusAddress))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(Postal))
    f.write("{}, ".format(PhoneNum))
    f.write("{}, ".format(NumCars))
    f.write("{}, ".format(ExtraLiability))
    f.write("{}, ".format(OptLoanCar))
    f.write("{}, ".format(OptGlassCost))
    f.write("{}, ".format(PayOption))
    f.write("{}\n, ".format(FV.FDollar2(TotFullCost)))
    f.close()
    print()
    print("Policy Information Processed and Saved.")
    POLICY_NUM += 1
