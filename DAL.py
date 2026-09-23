import sqlite3

def get_connection():
    """Function to connect to the database"""
    conn = sqlite3.connect('warehouseDB')
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def getAllOwners():
    """Function to get all owners for printing"""
    rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM Owner
        ''')

        rows = cursor.fetchall()
    except sqlite3.IntegrityError as e:
        print(f"Failed to get all owners: {e}")
    finally:
        conn.close()
    return rows


def showPaymentHistory(ownerId):
    rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT *
                       FROM Payment
                       WHERE owner_id = ?
                       ''', (ownerId,))

        rows = cursor.fetchall()
    except sqlite3.IntegrityError as e:
        print(f"Failed to get payment history: {e}")
    finally:
        conn.close()
    return rows



def viewCurrentHoldings(ownerId):
    rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT *
                       FROM Locker
                       WHERE owner_id = ?
                       ''', (ownerId,))

        rows = cursor.fetchall()
    except sqlite3.IntegrityError as e:
        print(f"Failed to get payment history: {e}")
    finally:
        conn.close()
    return rows


def getAllFacilities(companyId):
    rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT *
                       FROM Facility
                        WHERE company_id = ?
                       ''', (companyId,))

        rows = cursor.fetchall()
    except sqlite3.IntegrityError as e:
        print(f"Failed to get all facilities: {e}")
    finally:
        conn.close()
    return rows


def getAllCompanies():
    """Function to get all companies for printing"""
    rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT *
                       FROM Company
                       ''')

        rows = cursor.fetchall()
    except sqlite3.IntegrityError as e:
        print(f"Failed to get all companies: {e}")
    finally:
        conn.close()
    return rows


def changeOwner(lockerId, owner):
    """Function to change ownership of locker using a new owner's id"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE Locker
        SET owner_id = ?
        WHERE locker_id = ?
        ''', (owner, lockerId))

        conn.commit()
        print("Owner successfully changed.")
    except sqlite3.IntegrityError as e:
        print(f"Failed to change owner: {e}")
    finally:
        conn.close()


def addItem(lockerId, itemName, itemCategory, itemValue):
    """Function to add item to locker using parameters"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO Items (locker_id, name, type, value)
        VALUES (?, ?, ?, ?)
        ''', (lockerId, itemName, itemCategory, itemValue))

        conn.commit()
        print("Item successfully added.")
    except sqlite3.IntegrityError as e:
        print(f"Failed to add item: {e}")
    finally:
        conn.close()


def removeItem(lockerId, itemId):
    """Function to remove specified item from specified locker"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        DELETE FROM Items
        WHERE locker_id = ? AND items_id = ?
        ''', (lockerId, itemId))

        conn.commit()
        print("Item successfully removed.")
    except sqlite3.IntegrityError as e:
        print(f"Failed to remove item: {e}")
    finally:
        conn.close()


def getAllItems(lockerId):
    """Function to get all items for a locker"""
    rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT *
                       FROM Items
                          WHERE locker_id = ?
                          ''', (lockerId,))

        rows = cursor.fetchall()
    except sqlite3.IntegrityError as e:
        print(f"Failed to get all items: {e}")
    finally:
        conn.close()
    return rows


def modifyItem(lockerId, itemId, newName, newCategory, newValue):
    """Function to modify item in locker using new parameters"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        UPDATE Items
        SET name = ?, type = ?, value = ?
        WHERE locker_id = ? AND items_id = ?
        ''', (newName, newCategory, newValue, lockerId, itemId))

        conn.commit()
        print("Item successfully modified.")
    except sqlite3.IntegrityError as e:
        print(f"Failed to modify item: {e}")
    finally:
        conn.close()


def addFacility(facilityName, location, companyId, size):
    """Function to take parameters from method to create facility"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO Facility (name, company_id, location, size)
        VALUES (?, ?, ?, ?)
        ''', (facilityName, companyId, location, size))

        conn.commit()
        print("Facility successfully added.")
    except sqlite3.IntegrityError as e:
        print(f"Failed to add facility: {e}")
    finally:
        conn.close()



def removeFacility(companyId, facilityId):
    """Function to remove facility based off facilityId and companyId"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
        DELETE FROM Facility
        WHERE facility_id = ? AND company_id = ?
        ''', (facilityId, companyId))

        conn.commit()
        print("Facility successfully removed.")
    except sqlite3.IntegrityError as e:
        print(f"Failed to remove facility: {e}")
    finally:
        conn.close()
    return None


def getValue(lockerId):
    """Function to get sum of the value of the locker's items (through SUM)"""
    rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT SUM(value)
                       FROM Items
                       WHERE locker_id = ?
                       ''', (lockerId,))

        rows = cursor.fetchall()
    except sqlite3.IntegrityError as e:
        print(f"Failed to get value: {e}")
    finally:
        conn.close()
    return rows


def getAllLockers(ownerId, facilityId):
    """Function to get all lockers associated with a owner at a facility"""
    rows = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
                       SELECT *
                       FROM Locker
                       WHERE owner_id = ? AND facility_id = ?
                       ''', (ownerId,facilityId))

        rows = cursor.fetchall()
    except sqlite3.IntegrityError as e:
        print(f"Failed to get lockers: {e}")
    finally:
        conn.close()
    return rows