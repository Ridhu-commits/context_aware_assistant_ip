from intent import IntentDetector

detector = IntentDetector()

print("\nIntent Test Ready\n")

while True:
    text = input("You: ")
    intent = detector.detect_intent(text)
    print("Intent:", intent)