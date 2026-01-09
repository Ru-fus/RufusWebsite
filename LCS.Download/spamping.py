import time
from pynput import keyboard



TRIGGER_KEY = "up"

def send_sequence() -> None:
    ctrl = keyboard.Controller()
    # BASTA CHE MODIFICHIATE I MESSAGGI EVIDENZIATI PER PERSONALIZZARE 
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.03)
    ctrl.type("/all ?")        # MESSAGGIO
    time.sleep(0.03)
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.2)

    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.03)
    ctrl.type("/all ?")        # MESSAGGIO
    time.sleep(0.03)
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.2)

    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.03)
    ctrl.type("/all ?")        # MESSAGGIO
    time.sleep(0.03)
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.2)

    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.03)
    ctrl.type("/all ?")        # MESSAGGIO
    time.sleep(0.03)
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.2)

    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.03)
    ctrl.type("/all ?")        # MESSAGGIO
    time.sleep(0.03)
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.2)

    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.03)
    ctrl.type("/all ?")        # MESSAGGIO
    time.sleep(0.03)
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.2)

    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.03)
    ctrl.type("/all ?")        # MESSAGGIO
    time.sleep(0.03)
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.2)

    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.03)
    ctrl.type("/all ?")        # MESSAGGIO
    time.sleep(0.03)
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.2)

    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.03)
    ctrl.type("/all ?")        # MESSAGGIO
    time.sleep(0.03)
    ctrl.press(keyboard.Key.enter)
    ctrl.release(keyboard.Key.enter)
    time.sleep(0.2)




SPECIAL_KEY_ALIASES = {
    "enter": keyboard.Key.enter,
    "return": keyboard.Key.enter,
    "space": keyboard.Key.space,
    "tab": keyboard.Key.tab,
    "esc": keyboard.Key.esc,
    "escape": keyboard.Key.esc,
    "backspace": keyboard.Key.backspace,
    "delete": keyboard.Key.delete,
    "home": keyboard.Key.home,
    "end": keyboard.Key.end,
    "pageup": keyboard.Key.page_up,
    "pagedown": keyboard.Key.page_down,
    "up": keyboard.Key.up,
    "down": keyboard.Key.down,
    "left": keyboard.Key.left,
    "right": keyboard.Key.right,
    # Function keys
    "f1": keyboard.Key.f1,
    "f2": keyboard.Key.f2,
    "f3": keyboard.Key.f3,
    "f4": keyboard.Key.f4,
    "f5": keyboard.Key.f5,
    "f6": keyboard.Key.f6,
    "f7": keyboard.Key.f7,
    "f8": keyboard.Key.f8,
    "f9": keyboard.Key.f9,
    "f10": keyboard.Key.f10,
    "f11": keyboard.Key.f11,
    "f12": keyboard.Key.f12,
}


def parse_key(spec: str):
    s = (spec or "").strip().lower()
    if not s:
        return None
    if s in SPECIAL_KEY_ALIASES:
        return SPECIAL_KEY_ALIASES[s]
    # Single printable character
    if len(s) == 1:
        return keyboard.KeyCode.from_char(s)
    raise ValueError(
        f"Chiave non riconosciuta: {spec}. Usa tasti speciali (es. f8, enter) o un singolo carattere."
    )



def main() -> int:
    while True:
        try:
            trigger_key = parse_key(TRIGGER_KEY)
        except ValueError as e:
            print(e)
            return 2

        print(f"Premi '{TRIGGER_KEY}' per inviare la sequenza...")

        state = {"pressed": False, "is_sending": False}

        def is_trigger(k):
            return (
                k == trigger_key
                or (
                    isinstance(trigger_key, keyboard.KeyCode)
                    and isinstance(k, keyboard.KeyCode)
                    and getattr(k, "char", None) == trigger_key.char
                )
            )

        def on_press(key):
            if state["is_sending"]:
                return
            if is_trigger(key) and not state["pressed"]:
                state["pressed"] = True
                state["is_sending"] = True
                try:
                    send_sequence()
                finally:
                    state["is_sending"] = False
                # Ferma il listener dopo il primo invio
                return False


        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join()

        print("Sequenza inviata.")
        state["pressed"] = False

main()