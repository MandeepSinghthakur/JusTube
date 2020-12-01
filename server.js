var http = require('http'); // 1 - Import Node.js core module
var fs = require('fs')
var index = fs.readFileSync('index.html')
var server = http.createServer(function (req, res) {   // 2 - creating server
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end(index);

});

var io = require('socket.io')(http)

io.on('connection1',(socket) => {
	console.log('user1 has connected')
})



server.listen(8080); //3 - listen for any incoming requests

console.log('Node.js web server at port 8080 is running..')