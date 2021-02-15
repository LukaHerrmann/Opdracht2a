from pymongo import MongoClient


def getfirstitem(collection, rows):
    values = {}
    firstitem = collection.find_one()
    for row in rows:
        values[row] = firstitem[row]
    return values


def getfirstfiltered(collection, rows, filtername, filter):
    values = {}
    firstitem = collection.find_one({filtername: filter})
    for row in rows:
        values[row] = firstitem[row]
    return values


def average(collection, name, target):
    average = collection.aggregate([{'$group': {'_id': name, 'sum': {'$avg': target}}}])
    for avg in average:
        return avg


client = MongoClient()
db = client.huwebshop
print('De naam en prijs van het eerste product in de database: {}'.format(getfirstitem(db.products, ('name', 'price'))))
print('De naam van het eerste product dat begint met een \'R\': {}'.
      format(getfirstfiltered(db.products, ('name',), 'name', {'$regex':'^R'})))
print('De gemiddelde prijs van de producten in de database: {}'.format(average(db.products, 'price', '$price.selling_price')))
