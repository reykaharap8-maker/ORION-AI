
class Orion:
    def __init__(self):
        self.name = "ORION"
        self.version = "0.1.0"
        self.memory = []

    def think(self, message):
        self.memory.append({
            "role": "user",
            "content": message
        })

        response = (
            f"Aku {self.name}, "
            f"aku menerima pesanmu: {message}"
        )

        self.memory.append({
            "role": "assistant",
            "content": response
        })

        return response


if __name__ == "__main__":
    ai = Orion()

    print("ORION AI v0.1.0")
    print("Ketik 'exit' untuk keluar.")

    while True:
        message = input("\nYou: ")

        if message.lower() == "exit":
            print("ORION: Sampai jumpa!")
            break

        print("ORION:", ai.think(message))
