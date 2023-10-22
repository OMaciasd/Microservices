from app import create_app

app = create_app('default')  # o cualquier otro nombre de configuración que desees usar

if __name__ == '__main__':
    app.run()
