import sqlite3

def get_connection():
    conn = sqlite3.connect('warehouseDB')
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def getAllOwners():
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