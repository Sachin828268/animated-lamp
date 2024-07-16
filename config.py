import os
from pathlib import Path

class Config:
    
    API_ID = int(os.environ.get('20116095'))
    API_HASH = os.environ.get('3ed1ce1f57b104b5cbefebacc8c47e97')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    SESSION_NAME = os.environ.get('SESSION_NAME')
    USER_SESSION_STRING = os.environ.get('BQEy8n8APKVny0-hWlJ21MC2CZZHT_WehXRBNY7IRTv1KdDrZICHOayyyEZpd_su5qOrvNqi3ZSyJGxZAqYZ-7q2lxZdN6Y3SkcLx6BM-uEFY15RrCBQgym1Ym86OphZWGaZa1xQY5cekBfHXPEbO2JSdl1Q042J1ri6I2WtbPzOA58d-bXIajjmBIZY-lxMuWwaK6dHQz3QfHBIakVsPQdPnOkdHc2zbr7EzSTSdEnrRN81EK5QepbU0xkNoi_hKPvrHmvC5BRaAjJKqTH_bhYHczViXsmfQEeC8FDm4D50mYvwH5Vhnh3Gyb18uZ9dxr_M_BVhmhA1o8Ux_H0s50UJMhE15wAAAAGuWXyuAA')
    MIDDLE_MAN = int(os.environ.get('MIDDLE_MAN'))
    LINK_GEN_BOT = os.environ.get('LINK_GEN_BOT')
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL'))
    DATABASE_URL = os.environ.get('mongodb+srv://sachin0274936:chalubhaichecking@cluster0.q2sjjxz.mongodb.net/?retryWrites=true&w=majority')
    AUTH_USERS = [int(i) for i in os.environ.get('AUTH_USERS', '').split(' ')]
    
    SCRST_OP_FLDR = Path('screenshots/')
