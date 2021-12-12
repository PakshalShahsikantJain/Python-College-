
def Fibnoo(No) :
    Sum = 0;
    i = 0;
    no1 = 0;
    no2 = 1;

    print(no1,end = " ")
    print(no2,end = " ")
    for i in range(No) :
        Sum = no1 + no2;
        print(Sum,end = " ");
        no1 = no2;
        no2 = Sum;

        
def main() :
    print("Jay Ganesh...");
    No = 0
    print("Enter Number Till You Want Fibnoacci Series....");
    No = int(input());

    Fibnoo(No);

if __name__ == "__main__" :
    main()