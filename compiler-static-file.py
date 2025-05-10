from flask import Flask;
import os;
import server;
from distutils.dir_util import copy_tree;

ROOT_DIR=os.path.dirname(os.path.abspath(__file__));
OUTDIR=ROOT_DIR+"/docs";
IGNORE=("static","media");# Solo se copian y pegan.
server.rootPath="/Dabl03-shop-productos/";# Nombre del repositorio para evitar problemas.
def create_file(url:str,reponse):
  out_url=f"{OUTDIR}/{url if url!='/' else './index.html'}";
  print(f"Creando archivo {out_url}...");
  try:
    os.makedirs(os.path.dirname(out_url));
  except FileExistsError:
    pass;
  assert reponse.status_code>=200 and reponse.status_code<=299;
  with open(out_url,'wb') as out_file:
    out_file.write(reponse.get_data());
def compiler_url(app):
  with app.test_client() as client:
    for rule in app.url_map.iter_rules():
      #print(rule.endpoint)
      if IGNORE[0] not in rule.endpoint and IGNORE[1] not in rule.endpoint:
        url=str(rule);
        create_file(url,client.get(str(rule)));
  print("Copiando los directorios estaticos...");
  # copy_tree(f"{ROOT_DIR}/static",f"{OUTDIR}/static");
if __name__=="__main__":
  server.app.config["TEMPLATES_AUTO_RELOAD"]=False;
  server.app.config["DEBUG"]=False;
  #print(get_products().get_data())
  compiler_url(server.app);
  
