var TutorialToken = artifacts.require('TutorialToken');
const expect = require('expect');

contract('TutorialToken', function(accounts) {

  it('Name assert', async () => {
    var instance = await TutorialToken.deployed();
    // console.log(await instance.name.call());
    // assert.isTrue('TutorialToken' !== await instance.name.call())
    expect(await instance.name.call()).toBe('TutorialToken')
  })
});

// Solium -> Auditoria del contrato
// Solhint -> Linter