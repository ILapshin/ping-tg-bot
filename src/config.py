import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN=os.environ.get('BOT_TOKEN')
URL_LIST=os.environ.get('URL_LIST').split(',')
TIME_OFFSET=int(os.environ.get('TIME_OFFSET'))
USERS_FILE_PATH=os.environ.get('USERS_FILE_PATH')