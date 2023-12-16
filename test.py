from sqlalchemy import create_engine, inspect
 
# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'jatinjain'
host = '127.0.0.1'
port = 3306
database = 'hotwax'
 
# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
 
 
if __name__ == '__main__':
 
    try:
       
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        ins = inspect(engine)
        for table_name in ins.get_table_names():
            print(f' \n Table Name { table_name } \n')
            for column in ins.get_columns(table_name):
                print("Column: %s" % column['name'])
        print(
            f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)