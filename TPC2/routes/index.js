var express = require('express');
var router = express.Router();

/* GET home page. */

router.get(['/'], async function(req, res, next) {
  const cidades = await fetch("http://localhost:5000/cidades").then(response => response.json());
  res.render('index', { title: 'Cidades', cidades: cidades });
});


router.get('/:id', async function(req, res, next) {
  const cidade = await fetch(`http://localhost:5000/cidades/${req.params.id}`).then(response => response.json());
  
  const ligacoesFrom = await fetch(`http://localhost:5000/ligações?origem=${req.params.id}`).then(response => response.json());
  for (let i = 0; i < ligacoesFrom.length; i++) {
    ligacoesFrom[i] = await fetch(`http://localhost:5000/cidades/${ligacoesFrom[i].destino}`).then(response => response.json());
  }
  
  const ligacoesTo = await fetch(`http://localhost:5000/ligações?destino=${req.params.id}`).then(response => response.json());
  for (let i = 0; i < ligacoesTo.length; i++) {
    ligacoesTo[i] = await fetch(`http://localhost:5000/cidades/${ligacoesTo[i].origem}`).then(response => response.json());
  }

  const ligacoes = ligacoesFrom.concat(ligacoesTo);
  
  res.render('cidade', { cidade: cidade, ligacoesFrom: ligacoesFrom,ligacoesTo: ligacoesTo });
})
module.exports = router;
