def SumOfDigits(No) : 
    Digits = 0;
    Sum = 0;

    while No != 0 :
        Digits = No % 10;
        Sum = Sum + Digits;
        No = No // 10;
    
    return Sum;
    
def main() :
    No = 0;
    ret = 0;

    print("Jay Ganesh......");
    print("Enter One Number");
    No = int(input());

    ret = SumOfDigits(No);

    print("Addtion of Digits of Entered Number is : ",ret);

if __name__ == "__main__" :
    main()