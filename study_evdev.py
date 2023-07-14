
from evdev import InputDevice, categorize, ecodes

# Obtém o dispositivo de entrada do teclado
dev = InputDevice('/dev/input/event2')  # Substitua 'eventX' pelo dispositivo correto

# Loop principal
for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        if key_event.keystate == key_event.key_down:
            print("Tecla pressionada:", key_event.keycode)

