from flask import Blueprint, request, jsonify
from api.controllers.product import create_one, read_all, read_by_id, update_by_id, delete_by_id, json_to_table
import os

product = Blueprint('product', __name__)

# Add records from file
@product.route('/product/add_records_from_file', methods=['GET'])
def add_records_from_file():
  """"""
  return json_to_table('products.json')


# Create a Product
@product.route('/product', methods=['POST'])
def add_product():
  """"""
  return create_one(request)

# Get All Products
@product.route('/products', methods=['GET'])
def get_products():
  """"""
  return read_all(request)

# Get Single Products
@product.route('/product/<id>', methods=['GET'])
def get_product(id):
  """"""
  return read_by_id(request, id)

# Update a Product
@product.route('/product/<id>', methods=['PATCH'])
def update_product(id):
  """"""
  return update_by_id(request, id)

# Delete Product
@product.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  """"""
  return delete_by_id(request, id)