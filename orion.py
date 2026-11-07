
import requests

class Orion:
    def __init__(self):
        self.name = "ORION"
        self.model = "qwen2.5:1.5b"
        self.url = "http://localhost:11434/api/chat"

        self.memory = [
            {
                "role": "system",
                "content": (
                    "Your name is ORION. "
                    "You are an intelligent, friendly, "
                    "curious and thoughtful AI assistant. "
                    "Speak naturally and follow the user's language. "
                    "Your default language is Indonesian."
                )
            }
        ]

    def think(self, message):
        self.memory.append({
            "role": "user",
            "content": message
        })

        try:
            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "messages": self.memory,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()

            answer = response.json()["message"]["content"]

            self.memory.append({
                "role": "assistant",
                "content": answer
            })

            return answer

        except requests.exceptions.ConnectionError:
            self.memory.pop()
            return "Otak lokal belum terhubung. Pastikan Ollama berjalan."

        except requests.exceptions.RequestException as error:
            self.memory.pop()
            return f"Terjadi kesalahan koneksi: {error}"


if __name__ == "__main__":
    ai = Orion()

    print("ORION AI v0.2.0")
    print("Ketik 'exit' untuk keluar.")

    while True:
        message = input("\nYou: ")

        if message.lower() == "exit":
            print("ORION: Sampai jumpa!")
            break

        print("\nORION:", ai.think(message))
