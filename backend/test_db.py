import psycopg2

def test_connection():
    try:
        conn = psycopg2.connect(
            dbname="women_safety",
            user="women_safety_user",
            password="Sakshivk@2911",
            host="localhost",
            port="5432"
        )
        print("Successfully connected to the database!")
        conn.close()
    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    test_connection() 