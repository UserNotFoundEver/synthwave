let audioContext = new (window.AudioContext || window.webkitAudioContext)();

document.querySelectorAll('.key').forEach(key => {
    key.addEventListener('mousedown', () => playSynth(key.dataset.note));
    key.addEventListener('mouseup', stopSynth);
    key.addEventListener('mouseleave', stopSynth);
});

function playSynth(note) {
    let oscillator = audioContext.createOscillator();
    oscillator.type = 'sawtooth';
    oscillator.frequency.setValueAtTime(getFrequency(note), audioContext.currentTime);

    let gainNode = audioContext.createGain();
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);

    oscillator.start();
    key.oscillator = oscillator;
}

function stopSynth(event) {
    if (event.target.oscillator) {
        event.target.oscillator.stop();
        event.target.oscillator.disconnect();
    }
}

function getFrequency(note) {
    const A4 = 440;
    const notes = {
        'C': -9, 'C#': -8, 'D': -7, 'D#': -6, 'E': -5, 'F': -4,
        'F#': -3, 'G': -2, 'G#': -1, 'A': 0, 'A#': 1, 'B': 2,
        'C2': 3, 'C#2': 4, 'D2': 5, 'D#2': 6
    };
    return A4 * Math.pow(2, (notes[note] / 12));
}
