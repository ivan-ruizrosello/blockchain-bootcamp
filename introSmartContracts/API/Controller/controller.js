var sc = require('jseth');
var fs = require('fs');

var Web3 = require('web3')
var web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));

// console.log(sc.checkWeb3Instance, 'e');
console.log( 'e');

sc.setProvider();
var myFirstContract;
var truffleBuild = JSON.parse(fs.readFileSync('./build/contracts/myFirstContract.json', 'utf8'));
console.log('-> ', truffleBuild.networks[web3.version.network].address)
sc.jsethContractFromTruffle(truffleBuild,(err,res)=>{
  if(err== null){ 
    myFirstContract = res;    
    console.log('NO ERROR');

  } else { 
    // console.log('ERROR', err)
    console.log('ERR => ', err);
  }
});


exports.send = function(req, res) {
  myFirstContract.instance.send(req.body.address,req.body.amount, {from:req.body.sender, gas:2000000});
  res.send("Sent");
};

exports.balanceOf = function(req, res) {
  var response;

  console.log('Address: ', `0x${req.params.address}`)
  //Adapatación de la llamada desde Postman para aceptar un address
  var address = "0x" + JSON.stringify(req.params.address).slice(1,JSON.stringify(req.params.address).length-1);
  
  console.log('Address: ', `0x${req.params.address}`)
  console.log('Address: ', address)

  console.log(JSON.stringify(sc, null, 4));  
  console.log(sc);
  
  var web3 = sc.getWeb3Instance();
  response = myFirstContract.instance.getBalance(address, {from:web3.eth.accounts[0], gas:2000000});
  res.send(response);
};
