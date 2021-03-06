var express = require('express');

var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 4586);

app.get('/',function(req,res){
  res.render('home');
});

/*app.get('/show-data',function(req,res){
  var context = {};
  context.sentData = req.query.myData;
  res.render('show-data', context);
}); */

app.get('/home',function(req,res){
  var qParams = [];
  for (var p in req.query){
    qParams.push({'name':p,'value':req.query[p]})
  }
  var context = {};
  context.dataList = qParams;
  res.render('home', context);
});

app.post('/posthome', function(req,res){
  var qParams = [];
  for (var p in req.body){
    qParams.push({'body_name':p,'body_value':req.body[p]})
  }
  var context = {};
  context.dataList = qParams;
  res.render('posthome', context);
});

app.post('/posthome',function(req,res){
  var qParams = [];
  for (var p in req.query){
    qParams.push({'name':p,'value':req.query[p]})
  }
  var context = {};
  context.dataList = qParams;
  res.render('posthome', context);
});

app.use(function(req,res){
  res.status(404);
  res.render('404');
});

app.use(function(err, req, res, next){
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.render('500');
});

app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});