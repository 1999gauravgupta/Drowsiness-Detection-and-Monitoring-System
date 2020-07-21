from pymongo import MongoClient
from datetime import datetime
def graph():
    client = MongoClient('mongodb+srv://test:test@cluster0-mqtrw.mongodb.net/admin?retryWrites=true&w=majority')
    db = client.report
    users = db.users
    check=list(users.find())
    print(check)
    id=[]
    dates=[]
    for item in check:
        id.append(item['_id'])
        for i in item['yc']:
            if isinstance(i,str):
                if i not in dates:
                    dates.append(i)
            elif isinstance(i, list):
                if i[0] not in dates:
                    dates.append(i[0])

        for i in item['ec']:
            if isinstance(i,str):
                if i not in dates:
                    dates.append(i)
            elif isinstance(i, list):
                if i[0] not in dates:
                    dates.append(i[0])

    fhand = open('gline.js','w')
    fhand.write("gline = [ ['Date'")
    for i in id:
        fhand.write(",'"+i+"'")
    fhand.write("]")

    for date in dates:
        fhand.write(",\n['"+date+"'")
        for item in check:
            if isinstance(item['yc'][0],str):
                item['yc']=[item['yc']]
            if isinstance(item['ec'][0],str):
                item['ec']=[item['ec']]
            yc=dict(item['yc'])
            ec=dict(item['ec'])
            ycc=yc.get(date,0)
            ecc=ec.get(date,0)
            total=ecc+ycc
            fhand.write(","+str(total))
        fhand.write("]");
    fhand.write("\n];\n")
    fhand.close()
