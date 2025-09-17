# -API-address-book-construction
project-learning API construction with CRUD

Rubrica API (Contacts Book API)

Description
A simple **CRUD REST API** built with FastAPI to manage a contact list.  
Contacts are stored in a local `rubrica.json` file, which is automatically created and updated when new contacts are added, modified, or deleted.

Technologies
- Python 3
- FastAPI
- Pydantic
- JSON file storage

Endpoints
- `GET /` → return all contacts
- `GET /contatti/{nome}` → get a single contact by name
- `POST /contatti` → create a new contact
- `PUT /contatti/{nome}` → update an existing contact’s phone number
- `DELETE /contatti/{nome}` → delete a contact by name

#Example Requests

Create a new contact
```http
POST /contatti
{
  "nome": "luca",
  "telefono": "1234567890"
}
