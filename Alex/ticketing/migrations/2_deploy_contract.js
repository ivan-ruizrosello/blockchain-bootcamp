var TutorialToken = artifacts.require('TutorialToken');

module.exports = function(deployer) {
  // Use deployer to state migration tasks.
  deployer.deploy(TutorialToken);
};
