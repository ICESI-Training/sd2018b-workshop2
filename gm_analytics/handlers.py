import connexion

app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app.add_api('my_api.yaml')

if __name__ == "main":
    app.run(port=8000)
