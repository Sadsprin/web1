const express = require('express');
const session = require('express-session');
const MySQLStore = require('express-mysql-session')(session);
const app = express();
 

const option = {
	host: 'localhost',
	port: 3306,
	user: 'sadspring',
	password: 'lnb1092205!',
	database: 'sessionprac',
}

const sessionStore = new MySQLStore(option);

app.use(session({
    secret: 'asadlfkj!@#!@#dfgasdg',
    resave: false,
    saveUninitialized: true,
    store: sessionStore,
}));


app.get('/', async (req, res, next) => {
    if(req.session.num === undefined){
        req.session.num = 1;
    } else {
        req.session.num =  req.session.num + 1;
    }
    res.send(`Views : ${req.session.num}`);
})
 
app.listen(3000, function () {
    console.log('3000!');
});
