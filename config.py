import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "17472409")

API_HASH = os.environ.get("API_HASH", "f88f6e75e24743472483687be021b684")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5735569195:AAG7SbDuN5EIPFyTtgUj7DcKawgDNymQwu4") 

FORCE_SUB = os.environ.get("FORCE_SUB", None) 

DB_NAME = os.environ.get("DB_NAME","Filterbot75")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Nomenclature:Nomenclature@cluster0.jcvnj.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e7aba0e06227ffd054728.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1922130202').split()]
