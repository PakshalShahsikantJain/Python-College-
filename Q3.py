def Reverse(No) :
    Digits = 0; 

    print("Number After Reversing is : ");
    while No != 0 : 
        Digits = No % 10;
        print(Digits,end = "");
        No = No // 10;

def main() :
    No = 0;
    print("Jay Ganesh....");
    print("Enter Any Digits Number...");

    No = int(input());

    Reverse(No);

if __name__ == "__main__" :
    main()