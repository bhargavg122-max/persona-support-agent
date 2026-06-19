from src.persona_detector import detect_persona

while True:
    msg = input("Enter message: ")
    persona = detect_persona(msg)
    print("Detected Persona:", persona)