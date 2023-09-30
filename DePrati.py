from flask import Flask, jsonify
from dotenv import load_dotenv
from mongodb import client

load_dotenv()

app = Flask(__name__)


db = client.DarExam
collection = db.productos

@app.route('/fetch-and-store', methods=['GET'])
def fetch_and_store_data():
    # Tu código para obtener y almacenar datos en la base de datos (como se mostró en tu código anterior)

    return jsonify({"message": "Datos almacenados en MongoDB"})

@app.route('/get-productos', methods=['GET'])
def get_products():

    products = list(collection.find({}))

    # Convierte los documentos de MongoDB en un formato JSON
    product_list = []
    for product in products:
        product_list.append({
            "code": product["code"],
            "name": product["name"],
            "description": product["description"],
            "price": product["price"],
            #"stock_status": product["stock_status"]
        })

    return jsonify(product_list)

if __name__ == '__main__':
    app.run(debug=True)