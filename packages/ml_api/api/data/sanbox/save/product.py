from flask import jsonify
from api.data.models.products import Product, ProductSchema
from api.app import db
import json

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Populate database table from file
def json_to_table(relative_file_path):
  """"""
  try:
    json_array = json.load(open(relative_file_path))
    for item in json_array:
      name = item['name']
      description = item['description']
      price = item['price']
      qty = item['qty']
      new_product = Product(name, description, price, qty)
      db.session.add(new_product)
    db.session.commit()
    return '<h1>Records Added<h1>', 200
  except:
    return '<h1>Load Failed</h1>', 500

# Create a Product
def create_one(request):
  """"""
  try:
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product), 200
  except:
    return '<h1>Record Creation Failed</h1>', 500

def read_all(request):
  """"""
  try:
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result), 200
  except:
        return '<h1>Read All Failed</h1>', 500

def read_by_id(request, id):
  """"""
  try:
    product = Product.query.get(id)
    return product_schema.jsonify(product), 200
  except:
    return '<h1>Read By Id Failed</h1>', 500

def update_by_id(request, id):
  """"""
  try:
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()
    return product_schema.jsonify(product), 200
  except:
    return '<h1>Update By Id Failed</h1>', 500

def delete_by_id(request, id):
  """"""
  try:
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product), 200
  except:
    return '<h1>Delete By Id Failed</h1>', 500