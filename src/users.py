import os


def read_users(users_file_path):
        users = []

        if not os.path.exists(users_file_path):
            with open(users_file_path, 'x') as file:
                pass
            
        with open(users_file_path, 'r+') as file:
            users = [line.strip() for line in file] 
        return users


def write_user(users_file_path, user_id):
    with open(users_file_path, 'a+') as file:
        file.write(f'{user_id}\n')