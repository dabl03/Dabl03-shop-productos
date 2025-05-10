#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Blueprint, jsonify, Response;
from json import dumps as json_dumps;
import query;

#Constant:
DEBUG=False;
app = Flask(__name__);
root_program="./";
rootPath="/";# El archivo compiler-static-file.py lo modifica para no tener problema en github Page
production=None;
app.config["TEMPLATES_AUTO_RELOAD"]=True if DEBUG else None;
app.config["DEBUG"]=DEBUG;

#Registramos una nueva url
media_pt=Blueprint("media", __name__, static_folder=root_program+"/media", static_url_path="/media");
app.register_blueprint(media_pt);

def get_static_file(url):
  """Lee un archivo de texto y retorna su contenido.""";
  with open(root_program+url,'r') as file:
    return file.read();
  return "Error: File not Found";

@app.route("/")
def product():
  return render_template(
    "index.html",
    title="Productos disponible",
    name_logo="Dabl03",
    rootPath=rootPath
  );

@app.route("/productos.json",methods=['GET'])
def get_products():
  return Response(json_dumps(query.gdb_products('Si')), mimetype='application/json');

@app.route("/productos-not-available.json",methods=['GET'])
def get_products_not_available(available=1):
  return Response(json_dumps(query.gdb_products('No')), mimetype='application/json');

@app.errorhandler(404)
def not_found(error):
  return render_template('error.html'), 404;

if __name__ == '__main__':
  if DEBUG: production="localhost";
  else: production='0.0.0.0';
  app.run(host=production, port=5000);