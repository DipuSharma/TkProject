from tkinter import *
from PIL import ImageTk, Image


class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.title('Login Page')
        self.window.geometry('1368x768')
        self.window.resizable(0, 0)
        # self.window.attributes('-zoomed', True)
        self.window.state('iconic')

        """__________________Background Image___________________________"""
        self.bg_frame = Image.open('images/background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand=1)

        """--------------------------Login Frame-----------------------"""
        self.login_frame = Frame(self.window, bg='#040405', width='950', height=600)
        self.login_frame.place(x=200, y=70)

        self.text = "Welcome"
        self.heading = Label(self.login_frame, text=self.text, font=('Arial Black', 30, 'italic'), bg='#040405',
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

        self.sign_in_label = Label(self.login_frame, text='Sign In', bg='#040405', fg='white',
                                   font=('Time New Roman', 17, 'bold'))
        self.sign_in_label.place(x=680, y=130)

        """------------------------Username-------------------------------"""
        self.username_label = Label(self.login_frame, text='Username', bg='#040405',
                                    font=('Time New Roman', 12, 'bold'), fg='#4f4e4d')
        self.username_label.place(x=550, y=200, height=20)
        self.username_entry = Entry(self.login_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='white',
                                    font=('Time New Roman', 12, 'italic'))
        self.username_entry.place(x=580, y=230, width=270, height=20)
        self.username_line = Canvas(self.login_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=550, y=260)

        """-----------------------Username icon ------------------------"""
        self.username_icon = Image.open('images/username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.login_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=230)
        """------------------------Password-------------------------------"""
        self.password_label = Label(self.login_frame, text='Password', bg='#040405',
                                    font=('Time New Roman', 12, 'bold'), fg='#4f4e4d')
        self.password_label.place(x=550, y=280)
        self.password_entry = Entry(self.login_frame, highlightthickness=0, relief=FLAT, bg='#040405', fg='white',
                                    font=('Time New Roman', 12, 'italic'))
        self.password_entry.place(x=580, y=310, width=270, height=20)

        self.password_line = Canvas(self.login_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=550, y=340)

        """-----------------------Password icon ------------------------"""
        self.password_icon = Image.open('images/password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.login_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=310)

        """------------------------Login Button---------------------------"""
        self.login_button = Image.open('images/btn1.png')
        photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = Label(self.login_frame, image=photo, bg='#040405', bd=0, borderwidth=0, border=0)
        self.login_button_label.image = photo
        self.login_button_label.place(x=550, y=380)

        self.login = Button(self.login_button_label,
                            text='Login',
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

        """------------------------------Forgot Password---------------------------------"""
        self.forgot_password = Button(self.login_frame,
                                      text='Forgot Password ?',
                                      font=('arial', 10, 'underline'),
                                      fg='white',
                                      width=25,
                                      cursor='hand2',
                                      bg='#040405',
                                      activebackground='#040405',
                                      activeforeground='green',
                                      bd=0,
                                      highlightthickness=0,
                                      borderwidth=0
                                      )
        self.forgot_password.place(x=680, y=440)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage(file='images/show.png')

        self.hide_image = ImageTk.PhotoImage(file='images/hide.png')

        self.show_button = Button(self.login_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", bd=0)
        self.show_button.image = self.show_image
        self.show_button.place(x=860, y=310)

        """---------------------------Sign Up-------------------------------------------"""
        self.sign_label = Label(self.login_frame, text='No account yet?', font=("yu gothic ui", 12, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=500)

        photo = ImageTk.PhotoImage(file='images/register.png', size=15)
        self.signup_button_label = Button(self.login_frame,
                                          image=photo,
                                          bg='#98a65d',
                                          cursor="hand2",
                                          borderwidth=0,
                                          background="#040405",
                                          activebackground="#040405",
                                          highlightthickness=0,
                                          highlightcolor="white",
                                          highlightbackground="white")
        self.signup_button_label.image = photo
        self.signup_button_label.place(x=720, y=490, width=120, height=30)

    def show(self):
        self.hide_button = Button(self.login_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", bd=0)
        self.hide_button.place(x=860, y=310)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.login_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2", bd=0)
        self.show_button.place(x=860, y=310)
        self.password_entry.config(show='*')


def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()


if __name__ == '__main__':
    page()
