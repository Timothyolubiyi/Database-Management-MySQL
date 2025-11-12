import mysql.connector

def connect_mysql():
    """Connect to the MySQL server (no specific database needed)."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="TITAnic@2"
    )

def show_databases(cursor):
    """Show all databases."""
    cursor.execute("SHOW DATABASES")
    databases = [d[0] for d in cursor.fetchall()]
    print("\n📂 Available Databases:")
    for i, db in enumerate(databases, start=1):
        print(f"{i}. {db}")
    return databases

def drop_database(cursor, db_name):
    """Drop the selected database."""
    cursor.execute(f"DROP DATABASE IF EXISTS `{db_name}`")
    print(f"\n✅ Database '{db_name}' dropped successfully (if it existed).")

def main():
    try:
        conn = connect_mysql()
        cursor = conn.cursor()

        databases = show_databases(cursor)
        if not databases:
            print("⚠️ No databases found.")
            return

        choice = input("\nEnter the number of the database to delete: ").strip()
        if not choice.isdigit() or int(choice) not in range(1, len(databases)+1):
            print("❌ Invalid selection.")
            return

        db_to_drop = databases[int(choice)-1]

        # Safety check: don't allow system DBs to be dropped
        protected = {"mysql", "information_schema", "performance_schema", "sys"}
        if db_to_drop in protected:
            print(f"🚫 Cannot delete protected system database '{db_to_drop}'.")
            return

        confirm = input(f"⚠️ Are you SURE you want to permanently delete '{db_to_drop}'? (yes/no): ").strip().lower()
        if confirm == "yes":
            drop_database(cursor, db_to_drop)
        else:
            print("🚫 Operation cancelled.")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()
