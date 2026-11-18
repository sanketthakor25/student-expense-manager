
def student_expenses():
    print("\n=====Student Expences=====")
    
    expenses = []
    while True:
    
        amount = int(input("Enter expenses:\t"))
        category = input("Enter Category:\t")
        description = input("Enter description:\t")
        expenses.append([amount,category,description])
    
        print("Expenses Added!")
        print("\n===Expenses Detail===\n")
    
        print("Amount:\t",amount)
        print("Category:\t",category)
        print("Description:\t",description)
    
        # print("Do you want to add another expenses?")
        choice = input("\nAdd another expenses? (yes/no): \t").strip().lower()
    
    
        if choice =="no":
            break
        
        elif choice == "yes":
            continue
        
        else:
            print("Invalid choice!!!")
            
        print("\n===All Expenses===")    
        
        for expense in expenses:
            print("Amount:", expense[0])
            print("Category:", expense[1])
            print("Description:", expense[2])
            print("\n-------------------\n")
    total(expenses)     
    category_total(expenses) 
          
def total(total_expenses):
    total_amount = 0
    
    for expense in total_expenses:
        total_amount = total_amount + expense[0]
        
    print("Total expenses:",total_amount)  
    
def category_total(expenses):   
    category_expenses = {}
    
    for expense in expenses:
        
        category = expense[1]
        amount = expense[0]
        
        if category in category_expenses:
            category_expenses[category] += amount
        else:
             category_expenses[category] = amount
             
    print("\n===== Category Wise Expenses =====\n")         
            
    for category, amount in category_expenses.items():
        print(category, ":" , amount)
                



student_expenses()
