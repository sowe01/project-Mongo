
#para poder traer el database
def connectCollection(database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll

#para cambiar la columna a float y poder operar con ella
def change(value):
    cambio = {'€' : 1.09}
    value_n = {'B' : 10**9, 'M' : 10**6 , 'K' : 10**3}
    moneda = value[0]
    n = value[-1].upper()
    pp = re.findall("[0-9\.]{1,}",value)[0]
    pp = float(pp)
    return pp*value_n.get(n,1)*cambio.get(moneda,1)

#conocer las coordenadas de un sitio
def geocode(address):
    data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }
#hace las peticiones a la API de google
def requestMaps(radius,keyword,long,lat,tipo):
    token = os.getenv("API_KEY")
    if not token:
        raise ValueError("You must set a GITHUB_APIKEY token")
    baseUrl = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={token}&location={lat},{long}&radius={radius}&type={tipo}&keyword={keyword}"
    url = baseUrl
    print(f"Requesting data from {url[:6]}")
    res = requests.get(url)
    if res.status_code != 200:
        print(res.text)
        raise ValueError("Bad Response")
    return res.json()