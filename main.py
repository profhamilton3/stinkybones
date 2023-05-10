def on_sound_loud():
    input.set_sound_threshold(SoundThreshold.LOUD, input.sound_level() + 50)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_received_string(receivedString):
    global SMELLS
    if receivedString == "XXX":
        SMELLS = False
    
radio.on_received_string(on_received_string)

SMELLS = False
radio.set_group(3)
input.set_sound_threshold(SoundThreshold.LOUD, 50)
radio.set_transmit_serial_number(True)
radio.set_transmit_power(3)
SMELLS = True
basic.show_leds("""
    . . . . .
        # . . . #
        # # # # #
        # . . . #
        . . . . .
""")

def on_forever():
    if SMELLS:
        radio.send_number(1)
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
basic.forever(on_forever)
