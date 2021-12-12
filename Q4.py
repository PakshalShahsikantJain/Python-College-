def ArmStrong(No) : 
    Digits = 0;
    Sum = 0;
    no = No;
    while no != 0 : 
        Digits = no % 10;
        Sum = Sum + (Digits * Digits * Digits);
        no = no // 10;

    if No == Sum :
        return True;
    else :
        return False;
        
def main() :
    No = 0;
    bret = False;

    print("Jay Ganesh....");
    print("Enter One Number...");
    No = int(input());

    bret = ArmStrong(No);

    if bret == True : 
        print("Number is ArmStrong Number...");
    else : 
        print("Number is Not An Armstrong Number...");

if __name__ == "__main__" :
    main()