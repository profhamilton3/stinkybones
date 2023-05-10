input.onSound(DetectedSound.Loud, function () {
    input.setSoundThreshold(SoundThreshold.Loud, input.soundLevel() + 50)
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "XXX") {
        SMELLS = false
    }
})
let SMELLS = false
radio.setGroup(3)
input.setSoundThreshold(SoundThreshold.Loud, 50)
radio.setTransmitSerialNumber(true)
radio.setTransmitPower(3)
SMELLS = true
basic.showLeds(`
    . . . . .
    # . . . #
    # # # # #
    # . . . #
    . . . . .
    `)
basic.forever(function () {
    if (SMELLS) {
        radio.sendNumber(1)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    }
})
