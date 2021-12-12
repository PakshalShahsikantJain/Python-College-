def Even(No) : 
    for i in range(No) :
        if i % 2 == 0 :
            print(i,end = " ");

def main() :
    No = 0;
    print("Jay Ganesh....");
    print("Enter Number Till You Only Even Numbers....");
    No = int(input());

    Even(No);

if __name__ == "__main__" :
    main()