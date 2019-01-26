const Web3 = require('web3');

const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));
const networkVersion = web3.version.network;

const address = '0x9e9340de71d11a08972eaeeaaf30a7e6f8d57f67';
const abi = [
	{
		"constant": true,
		"inputs": [],
		"name": "opened",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "closeDoor",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "openDoor",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "opened",
				"type": "bool"
			},
			{
				"indexed": false,
				"name": "owner",
				"type": "address"
			}
		],
		"name": "DoorStatus",
		"type": "event"
	}
]

const contract = web3.eth.contract(abi);
const contractInstance = contract.at(address);

const filter = { sender: 1 };
const options = {fromBlock: 25, toBlock: 'latest'}; 

contractInstance.DoorStatus(filter, options, (_error, result) => {
  console.log(result.args);
});