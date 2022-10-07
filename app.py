from flask import Flask


app = Flask(__name__)

@app.get("/")
def pokemon_list():
    return "Charmander, Pikachu, eevee, bulbasur, diglett"


@app.get("/bulbusuar")
def bulbusaur_data():
    return "This is bulbusuar, a generation 1 pokemon who looks like a little dinosaur"

@app.get("/charmander")
def charmander_data():
    return "This is charmander, a generation 1 pokemon who looks like a little reptile"

@app.get("/pikachu")
def pikachu_data():
    return "This is pikatchu r, a generation 1 pokemon who looks like a little dinosaur"

@app.get("/eevee")
def eevee_data():
    return "This is eevee, a generation 1 pokemon who looks like a little dinosaur"

@app.get("/diglett")
def diglett_data():
    return "This is diglett, a generation 1 pokemon who looks like a little dinosaur"

if __name__ == "__main__":
    app.run()

