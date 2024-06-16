import plyvel
import sys

def fetch_value_from_leveldb(db_path, key):
    # Open the LevelDB database
    db = plyvel.DB(db_path, create_if_missing=False)
    
    try:
        # Fetch the value for the given key
        value = db.get(key.encode('utf-8'))
        
        if value:
            return value.decode('utf-8')
        else:
            return None
    finally:
        # Always close the database
        db.close()

def fetch_all_records(db_path):
    # Open the LevelDB database
    db = plyvel.DB(db_path, create_if_missing=False)
    
    try:
        # store records
        records = []
        
        # Iterate over all key-value pairs in the database
        for key, value in db:
            records.append((key.decode('utf-8'), value.decode('utf-8')))
        
        return records
    finally:
        db.close()

def insert_data_into_db(db_path, key, value):
    # Open the LevelDB database
    db = plyvel.DB(db_path, create_if_missing=True)

    try:
        # Encode key and value as bytes
        key_bytes = key.encode('utf-8')
        value_bytes = value.encode('utf-8')

        # Put key-value pair into the database
        db.put(key_bytes, value_bytes)
        
        print(f"Inserted key '{key}' with value '{value}' into the database.")
    finally:
        # Always close the database
        db.close()


if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 2:
        print("the program will function on the basis of passed arguments\n\n")
        print("this will print out all the values:")
        print("Usage: python leveldb.py <db_path>\n")
        print("This will print out specific value of the key provided")
        print("second Usage: python leveldb.py <db_payh> <key>\n")
        print("this will add a key value pair into database")
        print("third usage: python leveldb.py <db_path> <key> <value>\n")
        sys.exit(1)
    
    db_path = sys.argv[1]


    if len(sys.argv) == 2:
      records = fetch_all_records(db_path)
      if records is not None:
        print("All records in the database:")
        for key, value in records:
          print(f"Key: '{key}', Value: '{value}'")

    elif len(sys.argv) == 3:
      key = sys.argv[2]
      specific_record = fetch_value_from_leveldb(db_path, key)
      if specific_record is not None:
        print(f"Value for key '{key}': {specific_record}")

    elif len(sys.argv) == 4:
      key = sys.argv[2]
      value = sys.argv[3]
      insert_data_into_db(db_path,key,value)
    else:
        print("No records found in the database.")


