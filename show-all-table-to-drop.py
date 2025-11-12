import mysql.connector

def connect_db():
    """Connect to the MySQL database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="TITAnic@2",
        database="cloudnetwork"
    )

def show_tables(cursor):
    """Display all tables in the database."""
    cursor.execute("SHOW TABLES")
    tables = [t[0] for t in cursor.fetchall()]
    if not tables:
        print("\n⚠️ No tables found in this database.")
        return []
    print("\n📋 Tables in the database:")
    for i, table in enumerate(tables, start=1):
        print(f"{i}. {table}")
    return tables

def drop_table(cursor, conn, table_name):
    """Drop a selected table."""
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()
    print(f"\n✅ Table '{table_name}' dropped successfully (if it existed).")

def main():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        tables = show_tables(cursor)
        if not tables:
            return

        choice = input("\nEnter the number of the table you want to drop: ").strip()
        if not choice.isdigit() or int(choice) not in range(1, len(tables)+1):
            print("❌ Invalid selection.")
            return

        table_to_drop = tables[int(choice)-1]
        confirm = input(f"⚠️ Are you sure you want to drop '{table_to_drop}'? (yes/no): ").strip().lower()
        if confirm == "yes":
            drop_table(cursor, conn, table_to_drop)
        else:
            print("🚫 Drop cancelled.")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
