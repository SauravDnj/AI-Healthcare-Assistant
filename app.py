import customtkinter as ctk
import threading
from openai_client import get_ai_response

# ── Theme ──────────────────────────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ── Constants ──────────────────────────────────────────────────────────────────
APP_TITLE  = "🏥  AI Healthcare Assistant"
APP_W, APP_H = 900, 700

QUICK_QUESTIONS = [
    "What are symptoms of diabetes?",
    "How to lower blood pressure naturally?",
    "What foods boost immunity?",
    "Signs of anxiety & how to manage it?",
    "How much sleep does an adult need?",
    "What is BMI and how is it calculated?",
]

DISCLAIMER = (
    "⚠️  This app provides general health information only and is NOT a substitute "
    "for professional medical advice, diagnosis, or treatment."
)

# ── Main Window ────────────────────────────────────────────────────────────────
class HealthcareApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(f"{APP_W}x{APP_H}")
        self.resizable(True, True)
        self.chat_history = []   # list of (role, text)
        self._build_ui()

    # ── UI Layout ──────────────────────────────────────────────────────────────
    def _build_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ── Sidebar ────────────────────────────────────────────────────────────
        sidebar = ctk.CTkFrame(self, width=220, corner_radius=0,
                               fg_color="#1a1a2e")
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_rowconfigure(10, weight=1)

        ctk.CTkLabel(sidebar, text="🏥 HealthAI",
                     font=ctk.CTkFont(size=22, weight="bold"),
                     text_color="#4fc3f7").grid(row=0, column=0,
                                                padx=20, pady=(25, 5))
        ctk.CTkLabel(sidebar, text="Your Medical Assistant",
                     font=ctk.CTkFont(size=11),
                     text_color="#90a4ae").grid(row=1, column=0,
                                                padx=20, pady=(0, 20))

        ctk.CTkLabel(sidebar, text="Quick Questions",
                     font=ctk.CTkFont(size=12, weight="bold"),
                     text_color="#b0bec5").grid(row=2, column=0,
                                                padx=20, pady=(10, 5))

        for i, q in enumerate(QUICK_QUESTIONS):
            # Truncate long labels for the sidebar button display
            label = q if len(q) <= 32 else q[:30] + "…"
            btn = ctk.CTkButton(
                sidebar, text=label, width=190, height=36,
                font=ctk.CTkFont(size=11),
                fg_color="#16213e", hover_color="#0f3460",
                anchor="w",
                command=lambda txt=q: self._quick_ask(txt)
            )
            btn.grid(row=3 + i, column=0, padx=15, pady=3)

        ctk.CTkButton(sidebar, text="🗑  Clear Chat", width=190,
                      fg_color="#b71c1c", hover_color="#d32f2f",
                      command=self._clear_chat).grid(row=10, column=0,
                                                     padx=15, pady=15,
                                                     sticky="s")

        # ── Main area ──────────────────────────────────────────────────────────
        main = ctk.CTkFrame(self, fg_color="#0d1117")
        main.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        main.grid_rowconfigure(1, weight=1)
        main.grid_columnconfigure(0, weight=1)

        # Header
        header = ctk.CTkFrame(main, height=60, fg_color="#161b22",
                               corner_radius=0)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(header, text="💬  Chat with AI Healthcare Assistant",
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color="#e3f2fd").grid(row=0, column=0,
                                                padx=20, pady=15,
                                                sticky="w")

        # Chat display
        self.chat_box = ctk.CTkTextbox(
            main, font=ctk.CTkFont(size=13), wrap="word",
            fg_color="#0d1117", text_color="#e0e0e0",
            state="disabled", corner_radius=0
        )
        self.chat_box.grid(row=1, column=0, sticky="nsew",
                           padx=10, pady=(5, 0))

        # Disclaimer bar
        ctk.CTkLabel(main, text=DISCLAIMER,
                     font=ctk.CTkFont(size=10), text_color="#ef9a9a",
                     wraplength=640).grid(row=2, column=0,
                                          padx=10, pady=(4, 0))

        # Input area
        input_frame = ctk.CTkFrame(main, fg_color="#161b22",
                                   corner_radius=12)
        input_frame.grid(row=3, column=0, sticky="ew",
                         padx=10, pady=10)
        input_frame.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Describe your symptoms or ask a health question…",
            font=ctk.CTkFont(size=13), height=45,
            fg_color="#21262d", border_color="#30363d",
            text_color="#e0e0e0"
        )
        self.entry.grid(row=0, column=0, sticky="ew",
                        padx=(10, 5), pady=10)
        self.entry.bind("<Return>", lambda e: self._send())

        self.send_btn = ctk.CTkButton(
            input_frame, text="Send ➤", width=90, height=45,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#1565c0", hover_color="#1976d2",
            command=self._send
        )
        self.send_btn.grid(row=0, column=1, padx=(0, 10), pady=10)

        # Welcome message
        self._append_message("assistant",
            "👋 Hello! I'm your AI Healthcare Assistant.\n\n"
            "I can help you with:\n"
            "  • Symptom information\n"
            "  • General health & wellness tips\n"
            "  • Diet, nutrition & lifestyle advice\n"
            "  • Understanding medical terms\n\n"
            "How can I help you today?")

    # ── Helpers ────────────────────────────────────────────────────────────────
    def _append_message(self, role: str, text: str):
        self.chat_box.configure(state="normal")
        if role == "user":
            self.chat_box.insert("end", "\n👤 You:\n", "user_tag")
            self.chat_box.insert("end", f"{text}\n")
        else:
            self.chat_box.insert("end", "\n🤖 HealthAI:\n", "bot_tag")
            self.chat_box.insert("end", f"{text}\n")
        self.chat_box.configure(state="disabled")
        self.chat_box.see("end")

    def _quick_ask(self, question: str):
        self.entry.delete(0, "end")
        self.entry.insert(0, question)
        self._send()

    def _clear_chat(self):
        self.chat_history.clear()
        self.chat_box.configure(state="normal")
        self.chat_box.delete("1.0", "end")
        self.chat_box.configure(state="disabled")
        self._append_message("assistant", "Chat cleared. How can I help you?")

    def _send(self):
        user_text = self.entry.get().strip()
        if not user_text:
            return
        self.entry.delete(0, "end")
        self.send_btn.configure(state="disabled", text="…")
        self._append_message("user", user_text)
        self.chat_history.append({"role": "user", "content": user_text})
        threading.Thread(target=self._fetch_response,
                         args=(user_text,), daemon=True).start()

    def _fetch_response(self, user_text: str):
        response = get_ai_response(self.chat_history)
        self.chat_history.append({"role": "assistant", "content": response})
        self.after(0, self._display_response, response)

    def _display_response(self, text: str):
        self._append_message("assistant", text)
        self.send_btn.configure(state="normal", text="Send ➤")


# ── Run ────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = HealthcareApp()
    app.mainloop()