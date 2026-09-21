import DAL as db


def clear_screen():
    for i in range(0,50):
        print()


def show_specific_owner_details():
    while True:
        clear_screen()
        owners = db.getAllOwners()
        for i, owner in enumerate(owners):
            print(f"{i + 1}. {owner[1]}")
        while True:
            try:
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
            except ValueError:
                print("Invalid choice. Please try again.")



def owner_menu():
    while True:
        clear_screen()
        print("""
Owner Menu
1. View all Owners
2. View Specific Owner Details
""")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        owners = db.getAllOwners()
                        for i, owner in enumerate(owners):
                            print(f"{i + 1}. {owner[1]}")
                        break
                    case 2:
                        show_specific_owner_details()
                        break
                    case 0:
                        return
                    case _:
                        print("Invalid choice. Please try again.")
                        break
            except ValueError:
                print("Invalid choice. Please try again.")


def view_locker_details(lockerId):
    items = db.getAllItems(lockerId)
    for item in items:
        print(f"Item: {item[1]}\n Value: {item[3]}\n Category: {item[2]}")
    sum = db.getValue(lockerId)[0]
    print(f"Total value in locker: {sum}")

def add_item(lockerId):
    while True:
        try:
            itemName = input("Enter item name: ")
            itemCategory = input("Enter item category: ")
            itemValue = int(input("Enter item value: "))
            db.addItem(lockerId, itemName, itemCategory, itemValue)
            print(f"Item {itemName} added to locker {lockerId}.")
            break
        except ValueError:
            print("Invalid inputs. Please try again.")


def remove_item(lockerId):
    while True:
        items = db.getAllItems(lockerId)
        for i, item in enumerate(items):
            print(f"{i + 1}. {item[1]} - {item[2]} - {item[3]}")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(items):
                    db.removeItem(lockerId, items[choice - 1][0])
                    print(f"Item {items[choice - 1][1]} removed from locker {lockerId}.")
                    break
                elif choice == 0:
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid inputs. Please try again.")



def modify_item(lockerId):
    while True:
        items = db.getAllItems(lockerId)
        for i, item in enumerate(items):
            print(f"{i + 1}. {item[1]} - {item[2]} - {item[3]}")
        while True:
            try:
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
            except ValueError:
                print("Invalid inputs. Please try again.")


def change_ownership(lockerId):
    while True:
        owners = db.getAllOwners()
        for i, owner in enumerate(owners):
            print(f"{i + 1}. {owner[1]}")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(owners):
                    db.changeOwner(lockerId, owners[choice - 1][0])
                    print(f"Ownership changed to {owners[choice - 1][1]}")
                    break
                elif choice == 0:
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid inputs. Please try again.")


def locker_selection_menu(ownerId, facilityId):
    while True:
        clear_screen()
        print("Which locker would you like to view?")
        lockers = db.getAllLockers(ownerId, facilityId)
        for i, locker in enumerate(lockers):
            print(f"{i + 1}. {locker[1]}")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(lockers):
                    locker_menu(lockers[choice - 1][0])
                elif choice == 0:
                    return
                else:
                    print("Invalid choice. Please try again.")
                    break
            except ValueError:
                print("Invalid inputs. Please try again.")

def locker_start_menu(facilityId):
    while True:
        clear_screen()
        print("Whose lockers would you like to view?")
        owners = db.getAllOwners()
        for i, owner in enumerate(owners):
            print(f"{i + 1}. {owner[1]}")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(owners):
                    locker_selection_menu(choice, facilityId)
                elif choice == 0:
                    return
                else:
                    print("Invalid choice. Please try again.")
                    break
            except ValueError:
                print("Invalid inputs. Please try again.")

def locker_menu(lockerId):
    while True:
        clear_screen()
        print("""
1. View Details
2. Add Item
3. Remove Item
4. Modify Items
5. Change Ownership
        """)
        while True:
            try:
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        view_locker_details(lockerId)
                        break
                    case 2:
                        add_item(lockerId)
                        break
                    case 3:
                        remove_item(lockerId)
                        break
                    case 4:
                        modify_item(lockerId)
                        break
                    case 5:
                        change_ownership(lockerId)
                        break
                    case 0:
                        return
                    case _:
                        print("Invalid choice. Please try again.")
                        break
            except ValueError:
                print("Invalid inputs. Please try again.")


def add_facility(companyId):
    while True:
        facilityName = input("Enter facility name: ")
        db.addFacility(facilityName, companyId)
        print(f"Facility {facilityName} added.")
        break


def remove_facility(companyId):
    while True:
        facilities = db.getAllFacilities(companyId)
        for i, facility in enumerate(facilities):
            print(f"{i + 1}. {facility[1]}")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(facilities):
                    db.removeFacility(facilities[choice - 1][0])
                    print(f"Facility {facilities[choice - 1][1]} removed.")
                    break
                elif choice == 0:
                    return
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid inputs. Please try again.")


def facility_menu(companyId):
    while True:
        clear_screen()
        facilities = db.getAllFacilities(companyId)
        for i, facility in enumerate(facilities):
            print(f"{i + 1}. {facility[1]}")
        print(str(len(facilities) + 1) + ". Add Facility")
        print(str(len(facilities) + 2) + ". Remove Facility")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(facilities):
                    locker_start_menu(choice)
                    break
                elif choice == len(facilities) + 1:
                    add_facility(companyId)
                    break
                elif choice == len(facilities) + 2:
                    remove_facility(companyId)
                    break
                elif choice == 0:
                    return
                else:
                    print("Invalid choice. Please try again.")
                    break
            except ValueError:
                print("Invalid inputs. Please try again.")

def company_menu():
    while True:
        clear_screen()
        companies = db.getAllCompanies()
        for i, company in enumerate(companies):
            print(f"{i + 1}. {company[1]}")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(companies):
                    facility_menu(choice)
                    break
                elif choice == 0:
                    return
                else:
                    print("Invalid choice. Please try again.")
                    break
            except ValueError:
                print("Invalid inputs. Please try again.")


def main():
    while True:
        clear_screen()
        print("""
Warehouse Management System
1. Owner Menu
2. Company Menu
(! Hint: Enter 0 to go back to the previous menu)
        """)
        while True:
            try:
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        owner_menu()
                        break
                    case 2:
                        company_menu()
                        break
                    case _:
                        print("Invalid choice. Please try again.")
                        break
            except ValueError:
                print("Invalid inputs. Please try again.")
                


main()