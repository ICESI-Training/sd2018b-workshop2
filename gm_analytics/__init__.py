import connexion

app = connexion.FlaskApp(__name__, specification_dir='swagger/')
app.add_api('indexer.yml')

if __name__ == "main":
    app.run(port=8080)
