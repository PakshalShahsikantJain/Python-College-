def Pattern(Row,Col) :
    
    for i in range(1,Row + 1) :
        for j in range(1,Col + 1) :
            if i < j : 
                print(" ",end = "");
            else :  
                print(i," ",end = "");
        print("\r");

def main() :
    Row = 0;
    Col = 0;

    print("Jay Ganesh....");

    print("Enter Number of Rows You Want....");
    Row = int(input());

    print("Enter Number of Columns You Want...");
    Col = int(input());

    Pattern(Row,Col);

if __name__ == "__main__" :
    main()