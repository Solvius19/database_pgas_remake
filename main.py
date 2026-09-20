import DAL as db


def clearScreen():
        print()


def showSpecificOwnerDetails():
    while True:
        clearScreen()
        owners = db.getAllOwners()
        for i, owner in enumerate(owners):
            print(f"{i + 1}. {owner[1]}")
        while True:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(owners):
                ownerId = owners[choice - 1][0]
                print(f"Owner Name: {owners[choice - 1][1]}")
                print(f"Owner Email: {owners[choice - 1][2]}")
                print("\nCurrent Holdings:")
                holdings = db.viewCurrentHoldings(ownerId)
                for holding in holdings:
                    value = db.getValue(holding[0])
                    print(f"Locker ID: {holding[0]}, Company ID: {holding[3]}, Current Value: ${value[0]}")
                print("\nPayment History:")
                payments = db.showPaymentHistory(ownerId)
                for payment in payments:
                    print(f"Payment ID: {payment[0]}, Locker: {payment[2]}, Amount: {payment[3]}")
                break
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please try again.")


def ownerMenu():
    while True:
        print("""
Owner Menu
1. View all Owners
2. View Specific Owner Details
""")
        while True:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    db.getAllOwners()
                case 2:
                    showSpecificOwnerDetails()
                case 0:
                    return
                case _:
                    print("Invalid choice. Please try again.")
                    break


def viewLockerDetails(lockerId):
    items = db.getAllItems(lockerId)
    for item in items:
        print(f"Item: {item[1]}\n Value: {item[3]}\n Category: {item[2]}")
    sum = db.getValue(lockerId)[0]
    print(f"Total value in locker: {sum}")

def addItem(lockerId):
    while True:
        itemName = input("Enter item name: ")
        itemCategory = input("Enter item category: ")
        itemValue = int(input("Enter item value: "))
        db.addItem(lockerId, itemName, itemCategory, itemValue)
        print(f"Item {itemName} added to locker {lockerId}.")
        break


def removeItem(lockerId):
    while True:
        items = db.getAllItems(lockerId)
        for i, item in enumerate(items):
            print(f"{i + 1}. {item[1]} - {item[2]} - {item[3]}")
        while True:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(items):
                db.removeItem(lockerId, items[choice - 1][0])
                print(f"Item {items[choice - 1][1]} removed from locker {lockerId}.")
                break
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please try again.")



def modifyItem(lockerId):
    while True:
        items = db.getAllItems(lockerId)
        for i, item in enumerate(items):
            print(f"{i + 1}. {item[1]} - {item[2]} - {item[3]}")
        while True:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(items):
                newName = input("Enter new name: ")
                newCategory = input("Enter new category: ")
                newValue = int(input("Enter new value: "))
                db.modifyItem(lockerId, items[choice - 1][0], newName, newCategory, newValue)
                print(f"Item {items[choice - 1][1]} modified.")
                break
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please try again.")


def changeOwnership(lockerId):
    while True:
        owners = db.getAllOwners()
        for i, owner in enumerate(owners):
            print(f"{i + 1}. {owner[1]}")
        while True:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(owners):
                db.changeOwner(lockerId, owners[choice - 1][0])
                print(f"Ownership changed to {owners[choice - 1][1]}")
                break
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please try again.")


def lockerMenu(lockerId, companyId):
    while True:
        clearScreen()
        print("""
1. View Details
2. Add Item
3. Remove Item
4. Modify Items
5. Change Ownership
        """)
        while True:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    viewLockerDetails(lockerId)
                case 2:
                    addItem(lockerId)
                case 3:
                    removeItem(lockerId)
                case 4:
                    modifyItem(lockerId)
                case 5:
                    changeOwnership(lockerId)
                case 0:
                    return
                case _:
                    print("Invalid choice. Please try again.")
                    break


def addFacility(companyId):
    while True:
        facilityName = input("Enter facility name: ")
        db.addFacility(facilityName, companyId)
        print(f"Facility {facilityName} added.")
        break


def removeFacility(companyId):
    while True:
        facilities = db.getAllFacilities(companyId)
        for i, facility in enumerate(facilities):
            print(f"{i + 1}. {facility[1]}")
        while True:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(facilities):
                db.removeFacility(facilities[choice - 1][0])
                print(f"Facility {facilities[choice - 1][1]} removed.")
                break
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please try again.")


def facilityMenu(companyId):
    while True:
        clearScreen()
        facilities = db.getAllFacilities(companyId)
        for i, facility in enumerate(facilities):
            print(f"{i + 1}. {facility[1]}")
        print(str(len(facilities) + 1) + ". Add Facility")
        print(str(len(facilities) + 2) + ". Remove Facility")
        while True:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(facilities):
                lockerMenu(choice, companyId)
            elif choice == len(facilities) + 1:
                addFacility(companyId)
            elif choice == len(facilities) + 2:
                removeFacility(companyId)
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please try again.")
                break

def companyMenu():
    while True:
        clearScreen()
        companies = db.getAllCompanies()
        for i, company in enumerate(companies):
            print(f"{i + 1}. {company[1]}")
        while True:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(companies):
                facilityMenu(choice)
            elif choice == 0:
                return
            else:
                print("Invalid choice. Please try again.")
                break


def main():
    while True:
        print("""
Warehouse Management System
1. Owner Menu
2. Company Menu
(! Hint: Enter 0 to go back to the previous menu)
        """)
        while True:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    ownerMenu()
                case 2:
                    companyMenu()
                case _:
                    print("Invalid choice. Please try again.")
                    break
                


main()