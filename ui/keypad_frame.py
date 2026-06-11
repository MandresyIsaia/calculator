# ui/keypad_frame.py

import customtkinter as ctk
from config.theme import Theme
from config.buttons import BUTTONS_GRID, SHIFT_TRIG_MAP, SHIFT_FIRST_COL_MAP

class KeypadFrame(ctk.CTkFrame):
    def __init__(self, parent, on_button_click):
        super().__init__(parent, fg_color=Theme.BG_COLOR)
        self.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        self.on_button_click = on_button_click
        self.buttons_dict = {}
        
        self.create_buttons()

    def create_buttons(self):
        def lighten_color(color, factor=0.15):
            color = color.lstrip('#')
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            new_rgb = [min(int(c + (255 - c) * factor), 255) for c in rgb]
            return '#{:02x}{:02x}{:02x}'.format(*new_rgb)

        for row_idx, row in enumerate(BUTTONS_GRID):
            current_col = 0
            for col_idx, btn_text in enumerate(row):
                colspan = 4 if btn_text == "0" else 1
                if btn_text in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
                    bg_color = Theme.NUMBER_COLOR
                    text_color = "white"
                elif btn_text in ["+", "-", "*", "/", "=", "mod", "exp"]:
                    bg_color = Theme.ACCENT_COLOR
                    text_color = Theme.ACCENT_TEXT_COLOR
                elif btn_text in ["MC", "MR", "M+", "M-", "MS", "M▽"]:
                    bg_color = Theme.MEMORY_COLOR
                    text_color = "white"
                    
                else:
                    bg_color = Theme.BUTTON_COLOR
                    text_color = "white"

                hover_color = lighten_color(bg_color, 0.2)
                
                btn = ctk.CTkButton(
                    self, 
                    text=btn_text, 
                    width=60, 
                    height=45, 
                    fg_color=bg_color, 
                    text_color=text_color, 
                    hover_color=hover_color,
                    font=(Theme.FONT_FAMILY, Theme.BUTTON_FONT_SIZE), 
                    corner_radius=8,
                    command=lambda val=btn_text: self.on_button_click(val)
                )
                btn.grid(row=row_idx, column=current_col, columnspan=colspan,padx=4, pady=4, sticky="nsew")
                # self.buttons_dict[(row_idx, col_idx)] = btn
                
                btn.original_text = btn_text
                
                # Enregistrement dans le dictionnaire de référence
                self.buttons_dict[(row_idx, current_col)] = btn
                
                # On décale la colonne suivante en fonction de la place occupée
                current_col += colspan

        for r in range(len(BUTTONS_GRID)):
            self.grid_rowconfigure(r, weight=1)
        for c in range(len(BUTTONS_GRID[0])):
            self.grid_columnconfigure(c, weight=1)

    def update_key_labels(self, is_second):
        for (row_idx, col_idx), btn in self.buttons_dict.items():
            original_text = getattr(btn, "original_text", "")
            
            # Modification de la première colonne (col_idx == 0)
            if col_idx == 0 and original_text in SHIFT_FIRST_COL_MAP:
                new_text = SHIFT_FIRST_COL_MAP[original_text] if is_second else original_text
                btn.configure(text=new_text)
            
            # Modification des fonctions trigonométriques
            elif original_text in SHIFT_TRIG_MAP:
                new_text = SHIFT_TRIG_MAP[original_text] if is_second else original_text
                btn.configure(text=new_text)
                
            # Style visuel de la touche 2nd active/inactive
            elif original_text == "2nd":
                if is_second:
                    btn.configure(fg_color=Theme.ACCENT_COLOR, text_color=Theme.ACCENT_TEXT_COLOR)
                else:
                    btn.configure(fg_color=Theme.BUTTON_COLOR, text_color="white")

        # for (row_idx, col_idx), btn in self.buttons_dict.items():
        #     original_text = BUTTONS_GRID[row_idx][col_idx]
            
        #     # Changement de la première colonne
        #     if col_idx == 0 and original_text in SHIFT_FIRST_COL_MAP:
        #         new_text = SHIFT_FIRST_COL_MAP[original_text] if is_second else original_text
        #         btn.configure(text=new_text)
            
        #     # Changement des fonctions trigonométriques
        #     elif original_text in SHIFT_TRIG_MAP:
        #         new_text = SHIFT_TRIG_MAP[original_text] if is_second else original_text
        #         btn.configure(text=new_text)
                
        #     # Stylisation du bouton 2nd
        #     elif original_text == "2nd":
        #         if is_second:
        #             btn.configure(fg_color=Theme.ACCENT_COLOR, text_color=Theme.ACCENT_TEXT_COLOR)
        #         else:
        #             btn.configure(fg_color=Theme.BUTTON_COLOR, text_color="white")