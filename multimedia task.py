from tkinter import *
import webbrowser

# دالة لفتح الرابط من مربع الإدخال
def open_link():
    link = url_entry.get()
    if link:
        webbrowser.open(link)

# دالة لاختيار رابط جاهز
def choose_link():
    selected = link_choice.get()
    if selected == "google":
        url_entry.delete(0, END)
        url_entry.insert(0, "https://www.google.com")
    elif selected == "youtube":
        url_entry.delete(0, END)
        url_entry.insert(0, "https://www.youtube.com")

# دالة الخروج
def close_app():
    root.destroy()


root = Tk()
root.title("Mini Web Browser")
root.geometry("400x300")

#النص
title_label = Label(root, text="Mini Web Browser", font="Helvetica 16 bold", fg="blue")
title_label.pack(pady=10)

#دا المربع بتاع الرابط
url_entry = Entry(root, width=45)
url_entry.pack(pady=5)
#بيختار الروابط الجاهزه
link_choice = StringVar()
link_choice.set("google")
radio_google = Radiobutton(root, text="Google", variable=link_choice, value="google", command=choose_link)
radio_google.pack()
radio_youtube = Radiobutton(root, text="YouTube", variable=link_choice, value="youtube", command=choose_link)
radio_youtube.pack()

# زر فتح الرابط
open_btn = Button(root, text="Open Link", fg="white", bg="green", padx=10, pady=5, command=open_link)
open_btn.pack(pady=10)


exit_btn = Button(root, text="Exit", fg="white", bg="red", padx=10, pady=5, command=close_app)
exit_btn.pack(pady=5)

root.mainloop()
