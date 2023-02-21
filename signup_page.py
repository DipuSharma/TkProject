from tkinter import *
from PIL import ImageTk, Image


class SignUpForm:
    def __init__(self, window):
        self.window = window
        self.window.title('Registration Page')
        self.window.geometry('1368x768')

        """__________________Background Image___________________________"""
        self.bg_frame = Image.open('images/background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand=1)

        """--------------------------Login Frame-----------------------"""
        self.registration_frame = Frame(self.window, bg='#040405', width='950', height=600)
        self.registration_frame.place(x=200, y=70)

        self.text = "Welcome"
        self.heading = Label(self.registration_frame, text=self.text, font=('Arial Black', 30, 'italic'), bg='#040405',
                             fg='white')
        self.heading.place(x=100, y=30, width=300, height=30)

        """-------------------------Left Side Image------------------------"""
        """-------------------------Background Image-----------------------"""
        self.side_page = Image.open('images/vector.png')
        photo = ImageTk.PhotoImage(self.side_page)
        self.side_image_label = Label(self.window, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=220, y=150)

        """------------------------Sign In Image---------------------------"""
        self.sign_in_image = Image.open('images/hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.window, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=850, y=100)

        self.sign_in_label = Label(self.registration_frame, text='Sign Up', bg='#040405', fg='white',
                                   font=('Time New Roman', 17, 'bold'))
        self.sign_in_label.place(x=680, y=130)

        """------------------------Email-------------------------------"""
        self.email_label = Label(self.registration_frame, text='Email', bg='#040405',
                                 font=('Time New Roman', 12, 'bold'), fg='#4f4e4d')
        self.email_label.place(x=550, y=200, height=20)
        self.email_entry = Entry(self.registration_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='white',
                                 font=('Time New Roman', 12, 'italic'))
        self.email_entry.place(x=580, y=230, width=270, height=20)
        self.email_line = Canvas(self.registration_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.email_line.place(x=550, y=250)

        """------------------------Username-------------------------------"""
        self.username_label = Label(self.registration_frame, text='Username', bg='#040405',
                                    font=('Time New Roman', 12, 'bold'), fg='#4f4e4d')
        self.username_label.place(x=550, y=260, height=20)
        self.username_entry = Entry(self.registration_frame, highlightthickness=0, relief=FLAT, bg='#040405',
                                    fg='white',
                                    font=('Time New Roman', 12, 'italic'))
        self.username_entry.place(x=580, y=290, width=270, height=20)
        self.username_line = Canvas(self.registration_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=550, y=310)

        """------------------------Password-------------------------------"""
        self.password_label = Label(self.registration_frame, text='Password', bg='#040405',
                                    font=('Time New Roman', 12, 'bold'), fg='#4f4e4d')
        self.password_label.place(x=550, y=320)
        self.password_entry = Entry(self.registration_frame, highlightthickness=0, relief=FLAT, bg='#040405',
                                    fg='white',
                                    font=('Time New Roman', 12, 'italic'))
        self.password_entry.place(x=580, y=350, width=270, height=20)

        self.password_line = Canvas(self.registration_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=550, y=370)

        """------------------------Confirm Password-------------------------------"""
        self.password_label = Label(self.registration_frame, text='Confirm Password', bg='#040405',
                                    font=('Time New Roman', 12, 'bold'), fg='#4f4e4d')
        self.password_label.place(x=550, y=380)
        self.password_entry = Entry(self.registration_frame, highlightthickness=0, relief=FLAT, bg='#040405',
                                    fg='white',
                                    font=('Time New Roman', 12, 'italic'))
        self.password_entry.place(x=580, y=410, width=270, height=20)

        self.password_line = Canvas(self.registration_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=550, y=430)

        """------------------------Sign Up Button---------------------------"""
        self.login_button = Image.open('images/btn1.png')
        photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = Label(self.registration_frame, image=photo, bg='#040405', bd=0, borderwidth=0,
                                        border=0)
        self.login_button_label.image = photo
        self.login_button_label.place(x=550, y=450)

        self.login = Button(self.login_button_label,
                            text='Sign Up',
                            font=('Time New Roman', 12, 'bold'),
                            width=15,
                            bg='#3047ff',
                            cursor='hand2',
                            activebackground='#3047ff',
                            fg='white',
                            bd=0,
                            highlightthickness=0,
                            highlightcolor="white",
                            highlightbackground="white",
                            borderwidth=0)
        self.login.place(x=60, y=12)


signup_window = Tk()
SignUpForm(signup_window)
signup_window.mainloop()
