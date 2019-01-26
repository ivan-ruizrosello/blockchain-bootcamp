pragma solidity >=0.4.22 <0.6.0;


contract VaultDoor {
    bool public opened;
    address public owner;
    
    event DoorStatus(bool opened, address owner);
    
    modifier onlyOwner () {
        require(msg.sender == owner, "Only owner");
            
        _;
        
        emit DoorStatus(opened, owner);
    }
    
    constructor () public {
        owner = msg.sender;
        opened = false;
    }
    
    function openDoor() public onlyOwner {
        require(!opened, "The door is already opened");
        
        opened = true;
    }
    
    function closeDoor() public onlyOwner {
        require(opened, "The door is already closed");
        
        opened = false;
    }
}