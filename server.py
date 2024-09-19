#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Blueprint, jsonify, Response;
from json import dumps as json_dumps;
import query;

#Constant:
DEBUG=False;
app = Flask(__name__);
root_program="./";
production=None;

app.config["TEMPLATES_AUTO_RELOAD"]=True if DEBUG else None;
app.config["DEBUG"]=DEBUG;

#Registramos una nueva url
media_pt=Blueprint("media", __name__, static_folder=root_program+"/media", static_url_path="/media");
app.register_blueprint(media_pt);

def get_static_file(url):
  with open(root_program+url,'r') as html:
    return html.read();
  return "Error: Page no exists";
@app.route("/")
def product():
  return render_template("index.html",
    title="Productos disponible",
    name_logo="Dabl03");

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
  #https://es.stackoverflow.com/questions/436393/no-entiendo-bien-flask-host-y-puerto
  app.run(host=production, port=5000);