import main_credential_setup as cs

class PasswordDatabase:
    DATASTORE = "data.pwdb"
    title: str = None
    location: str = None
    credential_sets: list[cs.CredentialSet] = []
    
    def __init__(this):
        title: str = None
        location: str = None
        credential_sets: list[cs.CredentialSet] = []
    
    def create_database(this):
        print("Creating a new password database...")
        #Ask for title of database
        title = ""
        while title == "":
            title = this.__get_unique_database_name

        #Need to make sure the title is unique
        print("Let's set up the username for your new database...")
        username = input("Username: ")
        password = input("Password: ")
        #Need to verify the password since they cannot see it

        f = open(this.DATASTORE, 'a')
        f.write(f'{username},{password},{title}\n')
        f.close()
    
    def __get_unique_database_name(this):
        title = input("Type in name of new database: ")
        f = open(this.DATASTORE, 'r')
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            pieces = line.split(',')
            stored_title = pieces[2]
            if title.lower() == stored_title.lower():
                print("Invalid database name provided.")
                return ""
        f.close()
        return title








