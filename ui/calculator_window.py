# ui/calculator_window.py

import customtkinter as ctk
import os
from ui.display_frame import DisplayFrame
from ui.keypad_frame import KeypadFrame
from core.calculator_engine import CalculatorEngine
from config.theme import Theme

class MemoryHistoryWindow(ctk.CTkToplevel):
    def __init__(self, parent, history_list):
        super().__init__(parent)
        self.title("Historique Mémoire")
        self.geometry("350x400+0+0")
        self.configure(fg_color=Theme.BG_COLOR)
        
        self.transient(parent)
        self.grab_set()

        label = ctk.CTkLabel(
            self, 
            text="Historique de la Mémoire", 
            font=(Theme.FONT_FAMILY, 16, "bold"), 
            text_color=Theme.ACCENT_COLOR
        )
        label.pack(pady=15)

        textbox = ctk.CTkTextBox(self, font=(Theme.FONT_FAMILY, 13), fg_color="#1E1E1E", text_color="white")
        textbox.pack(fill="both", expand=True, padx=15, pady=10)

        if not history_list:
            textbox.insert("0.0", "Aucun état enregistré en mémoire pour le moment.")
        else:
            for item in reversed(history_list):
                textbox.insert("end", f"{item}\n")
        
        textbox.configure(state="disabled")

        btn_close = ctk.CTkButton(
            self, 
            text="Fermer", 
            fg_color=Theme.ACCENT_COLOR, 
            text_color=Theme.ACCENT_TEXT_COLOR,
            command=self.destroy
        )
        btn_close.pack(pady=15)


class CalculatorWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculatrice Scientifique")
        self.geometry("750x650+0+0")
        self.configure(fg_color=Theme.BG_COLOR)
        
        self.fullscreen = False
        self.bind("<F11>", self.toggle_fullscreen)

        if os.path.exists("calculator.ico"):
            self.iconbitmap('calculator.ico')

        self.engine = CalculatorEngine()
        self.display = DisplayFrame(self)
        self.keypad = KeypadFrame(self, on_button_click=self.on_key_press)

    def toggle_fullscreen(self, event=None):
        if not self.fullscreen:
            largeur = self.winfo_screenwidth()
            hauteur = self.winfo_screenheight()
            self.geometry(f"{largeur}x{hauteur-100}+0+0")
        else:
            self.geometry("750x650+0+0")
        self.fullscreen = not self.fullscreen

    def on_key_press(self, key_label):
        # 1. Gestion des modificateurs de mode
        if key_label == "2nd":
            is_active = self.engine.toggle_second()
            self.keypad.update_key_labels(is_active)
            return

        if key_label == "Rad/Deg":
            new_mode = self.engine.toggle_angle_mode()
            self.display.set_mode_label(new_mode.upper())
            return

        # 2. Gestion des commandes de mémoire
        if key_label in ["MC", "MR", "M+", "M-", "MS"]:
            self.engine.handle_memory(key_label)
            has_memory = self.engine.memory.recall() != 0.0
            self.display.set_memory_indicator(has_memory)
            
            if key_label == "MR":
                self.display.update_display(self.engine.token_manager.get_visual_expression())
            return

        if key_label == "M▽":
            history = self.engine.memory.get_history()
            MemoryHistoryWindow(self, history)
            return

        # 3. Validation de calcul et nettoyage
        if key_label == "=":
            result = self.engine.evaluate()
            self.display.update_display(self.engine.token_manager.get_visual_expression(), result)
            
            if self.engine.is_second_active:
                self.engine.toggle_second()
                self.keypad.update_key_labels(False)
            return

        if key_label == "CE":
            self.engine.clear_entry()
            self.display.update_display("0", "0")
            return

        if key_label == "⌫" or key_label == "C":
            self.engine.delete_last()
            vis = self.engine.token_manager.get_visual_expression()
            self.display.update_display(vis if vis else "0")
            return

        # 4. Traitement des entrées ordinaires / scientifiques
        resolved_key = key_label
        if self.engine.is_second_active:
            from config.buttons import SHIFT_TRIG_MAP, SHIFT_FIRST_COL_MAP
            if key_label in SHIFT_FIRST_COL_MAP:
                resolved_key = SHIFT_FIRST_COL_MAP[key_label]
            elif key_label in SHIFT_TRIG_MAP:
                resolved_key = SHIFT_TRIG_MAP[key_label]

        self.engine.add_input(resolved_key)
        self.display.update_display(self.engine.token_manager.get_visual_expression())