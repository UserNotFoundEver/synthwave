// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SynthWave {
    struct Synth {
        string name;
        uint256 frequency;
        string waveform;
        address owner;
    }

    Synth[] public synths;
    mapping(uint256 => address) public synthToOwner;
    mapping(address => uint256) ownerSynthCount;

    event NewSynth(uint256 synthId, string name, uint256 frequency, string waveform);

    function createSynth(string memory _name, uint256 _frequency, string memory _waveform) public {
        require(_frequency > 0, "Frequency must be greater than 0");
        synths.push(Synth(_name, _frequency, _waveform, msg.sender));
        uint256 id = synths.length - 1;
        synthToOwner[id] = msg.sender;
        ownerSynthCount[msg.sender]++;
        emit NewSynth(id, _name, _frequency, _waveform);
    }

    function getSynth(uint256 _synthId) public view returns (string memory, uint256, string memory, address) {
        Synth memory synth = synths[_synthId];
        return (synth.name, synth.frequency, synth.waveform, synth.owner);
    }

    function getOwnerSynths(address _owner) public view returns (uint256[] memory) {
        uint256[] memory result = new uint256[](ownerSynthCount[_owner]);
        uint256 counter = 0;
        for (uint256 i = 0; i < synths.length; i++) {
            if (synthToOwner[i] == _owner) {
                result[counter] = i;
                counter++;
            }
        }
        return result;
    }
}
