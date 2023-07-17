from bs4 import BeautifulSoup as BS
import requests
from tkinter import *

response = requests.get("https://news.ycombinator.com/news")
content = response.text

soup = BS(content, "html.parser")
name = soup.select(".titleline a" )

news_dict = {}
for links in range(0, 20, 2):
    news_dict.update({name[links].get_text():name[links].get("href")})

window = Tk()
window.title("NEWS HEADLINE")
window.maxsize(900, 700)

label = Label(text="Breaking News")
label.config(font=("Cursive", 30, "bold"), fg="black")
label.pack(side="top", padx=10, pady=10)

v = Scrollbar(orient="vertical")
t = Text(width=600, height=500, wrap="word", yscrollcommand=v.set)

for news, link in news_dict.items():
    t.config(font=("Cursive", 20, "bold"))
    t.insert(END, f"\tNEWS - {news} \n")
    t.config(font=("Cursive", 10, "bold"))
    t.insert(END, f"\tLINK - {link} \n\n")


v.config(command=t.yview)
t.pack(side="right", padx=10)
v.pack(side="left")




window.mainloop()




# from tkinter import ttk
# import tkinter as tk



# root = tk.Tk()
# container = ttk.Frame(root)
# container.pack()
# canvas = tk.Canvas(container)
# scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
# scrollable_frame = ttk.Frame(canvas)

# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )

# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# canvas.configure(yscrollcommand=scrollbar.set)


# x=ttk.Label(scrollable_frame, text="Sample scrolling label")
# x.place(x=50,y=50)


# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")

# root.mainloop()