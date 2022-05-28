class Development(Config):
    OWNER_ID = 808305342 # Su ID de telegram.
    OWNER_USERNAME = "hatake_sempai" # Su nombre de usuario de telegram.
    API_KEY = "5331784189:AAHQ8To-s-RibVY3aFokaJ9dXPtAkUVLA_s" # Su clave api, tal como la proporciona @botfather.
    SQLALCHEMY_DATABASE_URI = 'postgresql://nombredeusuario:contraseña@localhost:5432/database' # Credenciales de base de datos de muestra.
    MESSAGE_DUMP = '-721739978' # Algún chat grupal donde su bot este ahí.
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [808305342] # Lista de identificadores de usuarios que tienen acceso superusuario al bot.
    LOAD = []
    NO_LOAD = ['translation']
