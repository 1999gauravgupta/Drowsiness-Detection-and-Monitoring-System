const mongoose = require('mongoose')
var dc = require('../server')
const router = require('express').Router()

router.get('/' , (req,res)=> {
          user.find()
          .then(users => {
              res.status(200).json(users)
          })
          .catch(err=> {
              res.status(400).json(err)
          })
})

router.get('/add' , (req,res)=> {
        res.render('addition/adduser')
})
router.get('/data' , (req,res) => {
  console.log(dc)
})



module.exports = router