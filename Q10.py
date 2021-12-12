def Pattern(Row,Col) :
    
    for i in range(1,Row + 1) :
        for j in range(1,Col + 1) :
            if j == 4 :
                print((i + j) - 4, " ",end = "");
            elif j == 3 or j == 5 : 
                No = i;
                No = No - 1;
                if No <= 0 :
                    No = '';
                    print(No,"",end = "")
                print(No," ",end = ""); 
            elif j == 2 or j == 6 : 
                No = i;
                No = No - 2;
                if No <= 0 :
                    No = '';
                    print(No,"",end = "")
                print(No," ",end = "");
            elif j == 1 or j == 7 : 
                No = i;
                No = No - 3;
                if No <= 0 :
                    No = '';
                    print(No,"",end = "")
                print(No," ",end = ""); 
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