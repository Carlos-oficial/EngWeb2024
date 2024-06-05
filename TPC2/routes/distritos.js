var express = require('express');
var router = express.Router();

router.get('/:nome', async function(req, res, next) {
    const cidades = await fetch(`http://localhost:5000/cidades?distrito=${req.params.nome}`).then(response => response.json());    
    res.render('distrito', { nome:req.params.nome, cidades:cidades });
  })

module.exports = router;
