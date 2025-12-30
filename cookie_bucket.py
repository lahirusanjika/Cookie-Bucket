import requests
import customtkinter as ctk
from tkinter import messagebox
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CookieBucketApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Cookie Bucket Pro")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header Section
        header_frame = ctk.CTkFrame(self.root, fg_color="#1a1a2e", corner_radius=0)
        header_frame.pack(fill="x", padx=0, pady=0)
        
        title = ctk.CTkLabel(
            header_frame, 
            text="COOKIE BUCKET",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#00d9ff"
        )
        title.pack(pady=25)
        
        subtitle = ctk.CTkLabel(
            header_frame,
            text="Enterprise Authentication Management System",
            font=ctk.CTkFont(size=12),
            text_color="#6c757d"
        )
        subtitle.pack(pady=(0, 20))
        
        # Main Content
        content_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=30, pady=20)
        
        # Control Panel
        control_frame = ctk.CTkFrame(content_frame, fg_color="#1e1e1e", corner_radius=15)
        control_frame.pack(fill="x", pady=(0, 15))
        
        control_label = ctk.CTkLabel(
            control_frame,
            text="SELECT ACCOUNT TYPE",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#ffffff"
        )
        control_label.pack(pady=(20, 15), padx=20, anchor="w")
        
        # Button Container
        button_container = ctk.CTkFrame(control_frame, fg_color="transparent")
        button_container.pack(fill="x", padx=20, pady=(0, 20))
        
        # RSMY Button
        self.rsmy_btn = ctk.CTkButton(
            button_container,
            text="RSMY ACCOUNT",
            font=ctk.CTkFont(size=15, weight="bold"),
            height=50,
            fg_color="#0066cc",
            hover_color="#0052a3",
            corner_radius=10,
            command=lambda: self.get_cookie_and_copy("RSMY", self.rsmy_btn)
        )
        self.rsmy_btn.pack(side="left", expand=True, fill="x", padx=(0, 10))
        
        # Red Smith Button
        self.redsmith_btn = ctk.CTkButton(
            button_container,
            text="RED SMITH ACCOUNT",
            font=ctk.CTkFont(size=15, weight="bold"),
            height=50,
            fg_color="#0066cc",
            hover_color="#0052a3",
            corner_radius=10,
            command=lambda: self.get_cookie_and_copy("Red Smith", self.redsmith_btn)
        )
        self.redsmith_btn.pack(side="left", expand=True, fill="x", padx=(10, 0))
        
        # Status Section
        status_frame = ctk.CTkFrame(content_frame, fg_color="#1e1e1e", corner_radius=15)
        status_frame.pack(fill="x", pady=(0, 15))
        
        status_header = ctk.CTkLabel(
            status_frame,
            text="STATUS",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#6c757d"
        )
        status_header.pack(pady=(15, 5), padx=20, anchor="w")
        
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="Ready to retrieve authentication token",
            font=ctk.CTkFont(size=13),
            text_color="#28a745"
        )
        self.status_label.pack(pady=(0, 15), padx=20, anchor="w")
        
        # Output Section
        output_frame = ctk.CTkFrame(content_frame, fg_color="#1e1e1e", corner_radius=15)
        output_frame.pack(fill="both", expand=True)
        
        output_header = ctk.CTkLabel(
            output_frame,
            text="AUTHENTICATION TOKEN OUTPUT",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#6c757d"
        )
        output_header.pack(pady=(15, 10), padx=20, anchor="w")
        
        self.result_text = ctk.CTkTextbox(
            output_frame,
            font=ctk.CTkFont(family="Consolas", size=11),
            fg_color="#0d1117",
            border_color="#30363d",
            border_width=2,
            corner_radius=8,
            wrap="none"
        )
        self.result_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Footer
        footer = ctk.CTkLabel(
            self.root,
            text="v1.0.0 | Secure Token Management",
            font=ctk.CTkFont(size=10),
            text_color="#6c757d"
        )
        footer.pack(pady=(0, 10))
    
    def grab_cookie(self, cookie_type):
        """Grab cookie directly from paste2.org"""
        urls = {
            "RSMY": "https://gist.githubusercontent.com/lahirusanjika/e771eca9fea34d11fd09e53992bb93b2/raw/6839b30a687a49a03482420ff670c62a06a92482/rsmy_cookie.txt",
            "Red Smith": "https://gist.githubusercontent.com/lahirusanjika/de6336198f1518e66acf11899b63a505/raw/2d285039a2bf286f8748f692cb7464c0739d4916/redsmith_cookie.txt"
        }
        
        try:
            response = requests.get(urls[cookie_type], timeout=10)
            response.raise_for_status()
            cookie = response.text.strip()
            if not cookie:
                return "Error: Empty response from server"
            return cookie
        except requests.RequestException as e:
            return f"Error: Network error - {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_cookie_and_copy(self, cookie_type, button):
        """Get cookie and copy to clipboard"""
        def thread_function():
            self.root.after(0, lambda: self.status_label.configure(
                text=f"Retrieving {cookie_type} authentication token...",
                text_color="#ffc107"
            ))
            self.root.after(0, lambda: button.configure(state="disabled"))
            
            cookie = self.grab_cookie(cookie_type)
            
            self.root.after(0, lambda: self.update_result(cookie, cookie_type, button))
        
        threading.Thread(target=thread_function, daemon=True).start()
    
    def update_result(self, cookie, cookie_type, button):
        """Update the result in UI"""
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", cookie)
        
        if not cookie.startswith("Error"):
            self.root.clipboard_clear()
            self.root.clipboard_append(cookie)
            self.status_label.configure(
                text=f"Success: {cookie_type} token retrieved and copied to clipboard",
                text_color="#28a745"
            )
            messagebox.showinfo(
                "Operation Successful", 
                f"{cookie_type} authentication token has been copied to clipboard."
            )
        else:
            self.status_label.configure(
                text="Error: Failed to retrieve authentication token",
                text_color="#dc3545"
            )
            messagebox.showerror("Operation Failed", cookie)
        
        button.configure(state="normal")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CookieBucketApp()
    app.run()
