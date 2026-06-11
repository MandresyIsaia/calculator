# ui/display_frame.py

import customtkinter as ctk
from config.theme import Theme

class DisplayFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=Theme.BG_COLOR)
        self.pack(fill="x", padx=20, pady=(20, 10))

        # Indicateurs de statut
        self.status_frame = ctk.CTkFrame(self, fg_color=Theme.BG_COLOR)
        self.status_frame.pack(fill="x")

        self.memory_label = ctk.CTkLabel(
            self.status_frame, 
            text="", 
            font=(Theme.FONT_FAMILY, 14, "bold"), 
            text_color=Theme.ACCENT_COLOR
        )
        self.memory_label.pack(side="left", padx=10)

        self.mode_label = ctk.CTkLabel(
            self.status_frame, 
            text="RAD", 
            font=(Theme.FONT_FAMILY, 14, "bold"), 
            text_color=Theme.ACCENT_COLOR
        )
        self.mode_label.pack(side="right", padx=10)

        # Affichage de l'opération en cours
        self.operation_label = ctk.CTkLabel(
            self, 
            text="", 
            font=(Theme.FONT_FAMILY, Theme.OP_FONT_SIZE), 
            fg_color=Theme.BG_COLOR, 
            text_color="#888888", 
            anchor="e"
        )
        self.operation_label.pack(pady=(5, 5), padx=10, fill="x")

        # Container principal de résultat
        display_container = ctk.CTkFrame(self, fg_color=Theme.BG_COLOR)
        display_container.pack(fill="x")

        self.equal_sign = ctk.CTkLabel(
            display_container, 
            text="=", 
            font=(Theme.FONT_FAMILY, Theme.DISPLAY_FONT_SIZE_LARGE - 10), 
            text_color=Theme.ACCENT_COLOR
        )
        self.equal_sign.pack(side="left", padx=(0, 10))

        self.result_entry = ctk.CTkEntry(
            display_container, 
            font=(Theme.FONT_FAMILY, Theme.DISPLAY_FONT_SIZE_LARGE), 
            fg_color=Theme.BG_COLOR, 
            text_color=Theme.TEXT_COLOR, 
            border_width=0, 
            justify="right"
        )
        self.result_entry.pack(fill="x", expand=True)
        self.result_entry.insert(0, "0")
        self.result_entry.configure(state="readonly")

    def update_display(self, visual_expr, result_expr=None):
        self.operation_label.configure(text=visual_expr)
        
        if result_expr is not None:
            self.result_entry.configure(state="normal")
            self.result_entry.delete(0, ctk.END)
            self.result_entry.insert(0, result_expr)
            
            # Ajustement dynamique de la taille du texte
            if len(result_expr) > 12:
                self.result_entry.configure(font=(Theme.FONT_FAMILY, Theme.DISPLAY_FONT_SIZE_SMALL))
            else:
                self.result_entry.configure(font=(Theme.FONT_FAMILY, Theme.DISPLAY_FONT_SIZE_LARGE))
            self.result_entry.configure(state="readonly")

    def set_mode_label(self, mode_text):
        self.mode_label.configure(text=mode_text)

    def set_memory_indicator(self, active):
        self.memory_label.configure(text="M" if active else "")