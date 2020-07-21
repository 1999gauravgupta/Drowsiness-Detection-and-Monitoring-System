const express = require('express')
const mongoose = require('mongoose')
const keys = require('./config/keys_dev')
const exphbs = require('express-handlebars')
const adminRoutes = require('./routes/admin-routes')
const app = express()
const bodyParser = require('body-parser')
const path = require('path')
const SERVER_PORT = process.env.PORT || 5000


//mongoose.connect(keys.mongodb.dbURI, { useNewUrlParser: true ,useUnifiedTopology: true}).then(()=> {console.log('database connected sucessfully!!')}).catch(err=> console.log(err))
const MongoClient = require('mongodb').MongoClient
const url = 'mongodb+srv://testread:testread@cluster0-mqtrw.mongodb.net/admin?retryWrites=true&w=majority'
const assert = require('assert')
const dbName = 'report'
var dc;

app.use(express.static(path.join(__dirname , 'public')))

MongoClient.connect(url, function(err, client) {
  assert.equal(null, err);
  console.log("Connected successfully to server");

   const db = client.db(dbName);
  //console.log(db)
  const collection = db.collection('users');
  // Find some documents
  collection.find({}).toArray(function(err, docs) {
    assert.equal(err, null);
    console.log("Found the following records");
    //console.log(docs)
    dc = docs
    console.log(dc[0].yc[0][0])
  });

  client.close();
});



app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

app.engine('handlebars' , exphbs({
    defaultLayout:'main'
}))
app.set('view engine' ,'handlebars')

app.get('/' , (req,res)=> {
   res.render('index/homepage')
})

app.get('/welcome' , (req,res)=> {
          res.render('addition/dashboard')
})

app.get('/userlogin' , (req,res)=> {
         res.render('addition/login')
})

app.get('/usersignup' , (req,res)=> {
        res.render('addition/signup')
})
app.get('/adminlogin' , (req,res)=> {
       res.render('addition/loginadmin')
})

app.get('/team' , (req,res)=> {
       res.render('addition/team')
})
app.get('/summary' , (req,res)=> {
  res.render('addition/gline')
})

app.post('/adminlogin' , (req,res)=> {
        console.log(req.body)
         if(req.body.username == 'bitrebels' && req.body.password == 'bit123'){
          res.render('addition/users' , {
            data:dc
          })
         }else {
           res.send('login failure')
         }
        
})
app.listen(SERVER_PORT, (req,res) => {
     console.log('server started at port:' + SERVER_PORT)
})

module.exports = dc