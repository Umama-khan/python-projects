import tkinter as tk
import requests

class QuoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Quote of the Day")
        self.root.geometry("600x300")

        # Quote label
        self.quote_label = tk.Label(
            root,
            text="Fetching quote...",
            font=("Arial", 14),
            wraplength=550,
            justify="center"
        )
        self.quote_label.pack(pady=30)

        # Author label
        self.author_label = tk.Label(
            root,
            text="",
            font=("Arial", 12, "italic")
        )
        self.author_label.pack()

        # Next button
        self.next_button = tk.Button(
            root,
            text="Next Quote",
            command=self.fetch_quote
        )
        self.next_button.pack(pady=15)

        self.fetch_quote()  # Load first quote on start

    def fetch_quote(self):
        try:
            response = requests.get("https://api.quotable.io/random")
            data = response.json()

            quote = data["content"]
            author = data["author"]

            self.quote_label.config(text=f"“{quote}”")
            self.author_label.config(text=f"— {author}")
        except Exception as e:
            self.quote_label.config(text="Could not load quote.")
            self.author_label.config(text="Please check your internet.")

# --- Run the app ---
if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteApp(root)
    root.mainloop()

