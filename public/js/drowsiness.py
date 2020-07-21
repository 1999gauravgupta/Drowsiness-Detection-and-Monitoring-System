from pymongo import MongoClient
from datetime import datetime
def uptodate(id,now,yawn_count,eye_close):
    client = MongoClient('mongodb+srv://test:test@cluster0-mqtrw.mongodb.net/admin?retryWrites=true&w=majority')
    db = client.report
    date=now.strftime("%m/%d/%Y")
    users = db.users
    check=list(users.find({'_id':id}))
    s= dict()
    if len(check)==0:
        users.insert_one({'_id':id,'yc':list(s.items()),'ec':list(s.items())})
        check.append({'_id':id,'yc':list(s.items()),'ec':list(s.items())})
    check=check[0]
    update_yc=dict(check['yc'])
    update_ec=dict(check['ec'])
    update_yc[date]=update_yc.get(date,0)+yawn_count
    update_ec[date]=update_ec.get(date,0)+eye_close
    users.update_one({'_id':id},{'$set':{'yc':list(update_yc.items()),'ec':list(update_ec.items())}})



#uptodate("00x0001",'21-09-19',23,24)
#uptodate("00x0001",'22-09-19',23,24)
#uptodate("00x0002",'21-09-19',23,24)
