def student_expenses():
    print("\n===== Student Expenses =====\n")
    
    expenses = []
    while True:
        try:
            amount = int(input("Enter expenses amount:\t"))
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
            continue
            
        category = input("Enter Category:\t").strip()
        description = input("Enter description:\t").strip()
        
        expenses.append([amount, category, description])
    
        print("\nExpense Added Successfully!")
        print("---------------------------")
        print("Amount:\t\t", amount)
        print("Category:\t", category)
        print("Description:\t", description)
        print("---------------------------")
    
        choice = input("\nAdd another expense? (yes/no):\t").strip().lower()
    
        if choice == "no":
            break
        elif choice == "yes":
            continue
        else:
            print("Invalid choice! Please type 'yes' or 'no'.")
            
    # Display all recorded expenses before showing totals
    print("\n===== All Expenses Logged =====")
    for expense in expenses:
        print("Amount:\t\t", expense[0])
        print("Category:\t", expense[1])
        print("Description:\t", expense[2])
        print("-----------------------------")
        
    total(expenses)     
    category_total(expenses) 
          
def total(total_expenses):
    total_amount = 0
    for expense in total_expenses:
        total_amount += expense[0]
        
    print("\nTotal Expenses:", total_amount)  
    
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
        print(f"{category}: {amount}")

# Run the program
student_expenses()
