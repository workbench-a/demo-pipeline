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
  json_array = json.load(open(relative_file_path))
  for item in json_array:
    name = item['name']
    description = item['description']
    price = item['price']
    qty = item['qty']
    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
  db.session.commit()
  return '<h1>Records Added<h1>'

# Create a Product
def create_one(request):
  """"""
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  new_product = Product(name, description, price, qty)

  db.session.add(new_product)
  db.session.commit()

  return product_schema.jsonify(new_product)

def read_all(request):
  """"""
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result)
  # return jsonify(result.data)

def read_by_id(request, id):
  """"""
  product = Product.query.get(id)
  return product_schema.jsonify(product)

def update_by_id(request, id):
  """"""
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

  return product_schema.jsonify(product)

def delete_by_id(request, id):
  """"""
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)