from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import json

FILE_PATH = "rubrica.json"

def carica_dati():
   if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
     return json.load(f) # carica il file rubrica con tutti i dati aggiornati
   return {} 

def salva_dati():
   with open(FILE_PATH, "w") as f:
      json.dump(contatti,f,indent=4)

app = FastAPI(title="Rubrica API")

#qui contatti carica i suoi dati dal file json
contatti = carica_dati()

if not contatti:
 #se è la prima volta che apro il programma e non ci sono file contatti avra questi di partenza
 contatti: dict[str,str] = {"alessio"  :   "4534683853",
                            "maria"    :   "583958394",
                            "giovanni" :   "4848562"
                       }
 salva_dati()

class ContactIn(BaseModel):
   nome: str
   telefono : str

class contactupdate(BaseModel):
   telefono : str

#questa @app.get("/("radice")") mi riporta alla home della api ridandomi i contatti
@app.get("/")
def home():
    return contatti

#creo endpoint per cercare un contatto ora

@app.get("/contatti/{nome}")
def cerca_il_contatto(nome: str):
  nome = nome.lower()


   # controllo il contatto se c'è

  if nome in contatti:
    return {"nome": nome, "telefono" : contatti[nome]}

# se non esiste ritorno un errore http 404("il non trovato")
  else:
    raise HTTPException(status_code=404, detail="contact Not Found ")
  

@app.post("/contatti", status_code=201)
def crea_contatto(dati: ContactIn):
   nome = dati.nome.lower()
   if nome in contatti:
      raise HTTPException(status_code=400, detail="alredy existing")
   else:
      contatti[nome] = dati.telefono
      salva_dati()
   return {"messaggio ": "contatto creato con successo",
           "contatto" : {nome: dati.telefono}
          }

@app.delete("/contatti/{nome}")
def elimina_contatto(nome : str):
   if nome.lower() not in contatti:
    raise HTTPException(status_code=404, detail="nome non trovato riprova")
   else:
     del contatti[nome.lower()]
     salva_dati()
   return {"messaggio ": f"contatto '{nome}' eliminato con successo"}

@app.put("/contatti/{nome}")
def aggiorna_contatto(nome : str, dati : contactupdate):
   nome = nome.lower()

   #controllo se il nome è gia esistente con NOT quindi se il nome non è in contatti 404
   if nome not in contatti:
      raise HTTPException(status_code=404,detail="non trovato, riprova")
   else:
      contatti[nome] = dati.telefono
      salva_dati()
   return {"messaggio": f"Numero di '{nome}' aggiornato con successo", "contatto": {nome: dati.telefono}}
      
      

    
 
  