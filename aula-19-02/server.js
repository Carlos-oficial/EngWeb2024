var http = require('http')
var url = require('url')
var fs = require('fs')
http.createServer(function (req, res) {
    var q = url.parse(req.url, true)

    // console.log(q.pathname)
    fs.readFile('convert.py', function (err,dados){
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' })
        res.write(dados)
        res.end()
    })

}).listen(7777)