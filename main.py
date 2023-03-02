import time
import customtkinter
import tkinter as tk
from urllib.parse import urlparse
from PIL import ImageTk, Image


customtkinter.deactivate_automatic_dpi_awareness()

import json
f = open('storage.json') # Opening JSON file
data = json.load(f) # returns JSON object as a dictionary
eb = data['Websites']


import clr

def Home_Page():

    label_image = tk.Label(frame, border=0)
    label_image.place(relwidth=1, relheight=1)
    #label_image.config(image=img)
    pass



from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime
#clr.AddReference('System')
clr.AddReference('System.Windows.Forms') # load the .NET assembly for the System.Windows.Forms namespace
clr.AddReference('System.Threading') # load the .NET assembly for the System.Threading namespace.
from System.Windows.Forms import Control
from System.Threading import Thread,ApartmentState,ThreadStart



if not have_runtime():#There is no webview2 runtime or the version is too low
    install_runtime()#Download and install runtime

count  = 1
pause = "no"
save_url = None
top_webview = None
current_tabe = None
track_pair_widget = {}
track_pair_widget1 = {}
track_pair_widget2 = {}
track_pair_widget3 = {}


def Page_Title(url):
    p_title_= urlparse(url).hostname
    return p_title_.title()

def main():
    global count, pause
    global Visited_links
    global top_webview
    global current_tabe
    global track_pair_widget , track_pair_widget1, track_pair_widget2

    def Sytem_close():
        for child in app.winfo_children():  # destroy all child widgets of a frame:
            child.destroy()  # destroy all child widgets
            # shut down Python.NET

        app.destroy()

    def get_cur_url():
        while True:
            try:
                if top_webview.web_view.get_current_url() != None or top_webview.web_view.get_current_url() != search_url.get() :
                        search_url.set(top_webview.web_view.get_current_url())
                        #app.after(1000, lambda :[get_cur_url(), ex()])
                        track_pair_widget3[top_webview].config(text=Page_Title(top_webview.web_view.get_current_url()))
                        return
            except:
                return

            #app.after(3000, lambda: top_webview.evaluate_js('document.title', print))

    def save_site_fav_save():
        global save_url
        if save_url == None:
           save_url = search_url.get()
           save_site_fav.config(fg="red")

        print("s: ", save_url)


    def recall():
        global pause
        if pause == "yes":
                return
        if pause=="no":
                global count
                get_cur_url()
                app.after(4000, lambda :recall())

    def click_handler():
        global pause
        pause = "yes"

    def release_handler():
        global pause
        pause = "no"
        #time.sleep(1)
        app.after(10000, lambda :recall())

    def test_search(button,colorOnHover, colorOnLeave):  # Color change on Mouse Hover
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover,command=click_handler()))
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave,command=release_handler()))

    def Go_back():
            top_webview.web.GoBack()

    def Go_Forwad():
            top_webview.web.GoForward()

    def reload():
        top_webview.reload()

    def button_s(num):
        global top_webview
        # s_url = f'https://{search_url.get()}'
        s_url = f"https://www.google.com/search?q={search_url.get()}"

        print(search_url.get())
        print(top_webview)
        if top_webview == None:
            New_Tab_New_wind(s_url)
        else:
            try:
                top_webview.load_url(url=s_url)
                try:
                  track_pair_widget2[top_webview].config(text=Page_Title(s_url))
                except:
                    pass
            except:
                New_Tab_New_wind(s_url)


    def frame_changer(frame):
        frame.tkraise()

    def change_bg_OnHover(button, colorOnHover, colorOnLeave):  # Color change on Mouse Hover
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

    def change_fg_OnHover(button, colorOnHover, colorOnLeave):  # Color change on Mouse Hover
        button.bind("<Enter>", func=lambda e: button.config(fg=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(fg= colorOnLeave))

    def home_page(widg):
        global list_t, tr
        list_t = []
        tr = None

        def on_left_click(url):
            New_Tab_New_wind(url)

        def on_right_click():
            print("right_click")

        def refresh():
            i = 0
            while i < len(list_t):
                list_t[i].distroy()
                i += 1
            Home_Shortcuts()

        def test_search(button, i):  # Color change on Mouse Hover
            button.bind("<Button-1>", func=lambda e: button.config(command=on_left_click(i)))

        def test_search2(button):  # Color change on Mouse Hover
            button.bind("<Button-3>", func=lambda e: button.config(command=on_right_click()))

        f = open('storage.json')  # Opening JSON file
        data = json.load(f)  # returns JSON object as a dictionary
        eb = data['Websites']

        def Home_Shortcuts():
            global tr
            x_pos = 0.1
            y_pos = 0.1
            i = j = 0
            t = 0
            while j < 4:
                while i < 7:
                    if t < len(eb):
                        lab_1 = tk.Label(widg, bg='#B5A642', font=("Bauhaus 93", 17))
                        lab_1.place(relwidth=0.11, relheight=0.1, relx=x_pos, rely=y_pos)
                        lab_1.config(text=eb[t]['Name'])
                        change_bg_OnHover(lab_1, "#D2691E", "#B5A642" )
                        test_search(lab_1, eb[t]["Url"])
                        test_search2(lab_1)
                        list_t.append(lab_1)

                        t += 1
                    x_pos = x_pos + 0.12
                    i += 1

                y_pos += 0.2
                j += 1
                i = 0
                x_pos = 0.1


        Home_Shortcuts()


    def Home_show_Page():
        global top_webview
        #top_webview = Tab
        Home_Tab.tkraise()

    def New_Tab_New_wind(tab_url):
        global count
        global top_webview
        global current_tabe
        global track_pair_widget, track_pair_widget1, track_pair_widget2

        if track_pair_widget != {}:
            for x in track_pair_widget:
               track_pair_widget[x].configure(bg='#1C352D')

            for x in track_pair_widget1:
                   track_pair_widget1[x].configure(bg='#1C352D')


        def close_tab(t_num, w_num, t_nu):
            for child in t_num.winfo_children(): #  destroy all child widgets of a frame:
                child.destroy()  #  destroy all child widgets
            for child in w_num.winfo_children(): #  destroy all child widgets of a frame:
                child.destroy() #  destroy all child widgets
            t_num.destroy() #  destroy all frame widgets
            w_num.destroy() #  destroy all frame widgets

            track_pair_widget.pop(w_num)  #  Remove  widgets
            track_pair_widget1.pop(w_num) #  Remove  widgets
            track_pair_widget3.pop(t_nu)  #  Remove  widgets


        def Push_top(top_frame, top_web_view, tab_act):
            global top_webview
            top_frame.tkraise()    # push the frame window on top
            top_webview = top_web_view # assign the top_webview

            for x in track_pair_widget:
               track_pair_widget[x].configure(bg='#1C352D')

            for x in track_pair_widget1:
               track_pair_widget1[x].configure(bg='#1C352D')

            track_pair_widget[top_frame].configure(bg='#8A9A5B')
            track_pair_widget1[top_frame].configure(bg='#8A9A5B')


        # ======================  Creating a new web window =========================

        new_web_view_frame = tk.Frame(app)
        new_web_view_frame.place(y=30, relwidth=1, relheight=0.977)

        new_web_view = WebView2(new_web_view_frame, 500, 500)
        new_web_view.pack(fill="both", expand=True)
        new_web_view.load_url(tab_url)
        new_web_view_tab_title = Page_Title(tab_url) # getting the webpage title
        top_webview = new_web_view

        # ========================  Creating a new tab in the Tabs preview ==========

        new_tab_wid = tk.Frame(Tabs_view, bg='#232B2B')
        new_tab_wid.pack(side=tk.LEFT, fill='y', ipadx=60)
        change_bg_OnHover(new_tab_wid, 'yellow', '#232B2B')

        fr = tk.Frame(new_tab_wid, bg='gray')
        fr.place(relx=0.02, rely=0.02, relheight=0.98, relwidth=0.96)

        disp_tab = tk.Button(fr, text=f"{new_web_view_tab_title}", bg='#8A9A5B', anchor="w",borderwidth=0, border=0, activebackground="#27251F",  font=("Segoe Print Bold", 9), activeforeground="white", )
        disp_tab.place(relheight=1, relwidth=0.8, relx=0)
        track_pair_widget3[top_webview] = disp_tab
        track_pair_widget2[new_web_view] = disp_tab #pair ( top_web_window and  tab title)
        current_tabe = disp_tab
        disp_tab.configure(command=lambda:Push_top(new_web_view_frame, new_web_view, current_tabe))

        track_pair_widget[new_web_view_frame] = disp_tab # pair ( web_frame and associate tab)

        close_bt = tk.Button(fr, text="X", bg='#8A9A5B', activebackground='gray', activeforeground='red', borderwidth=0, border=0, font=("Consolas Bold", 11), command=lambda:close_tab(new_tab_wid,new_web_view_frame,top_webview))
        close_bt.place(relheight=1, relwidth=0.2, relx=0.8)
        track_pair_widget1[new_web_view_frame] = close_bt # pair ( web_frame and close tab)
        # ====


    app = tk.Tk()
    app.geometry("600x500")
    app.state("zoomed")
    app.title("Hezron Browser")

    app.iconbitmap("panda.ico")

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    search_url = tk.StringVar()

    # ===================== Navigation Bar Section ==========================================================================================================
    nav_bar_bg = "#232B2B"
    nav_bar = tk.Frame(app, bg=nav_bar_bg)
    nav_bar.place(x=0, y=0, relwidth=1, height=30)

    back_button = tk.Button(master=nav_bar, fg='white', text="⊂", font=("Courier New", 17), activebackground=nav_bar_bg, activeforeground='yellow'  , bg=nav_bar_bg, command=Go_back, border=0, borderwidth=0)
    back_button.place(relx=0.001, rely=0.1, relwidth=0.03, relheight=0.8)
    change_fg_OnHover(back_button, "yellow", "white")

    Next_button = tk.Button(master=nav_bar, fg='white',text="⊃", font=("Courier New", 17),activebackground=nav_bar_bg, activeforeground='yellow'  , bg=nav_bar_bg, command=Go_Forwad, border=0, borderwidth=0)
    Next_button.place(relx=0.031, rely=0.1, relwidth=0.03, relheight=0.8)
    change_fg_OnHover(Next_button, "yellow", "white")

    reload_button = tk.Button(master=nav_bar, fg='white',text="⟳", font=("Arial Bold", 15), activebackground=nav_bar_bg, activeforeground='yellow'  ,bg=nav_bar_bg,command=reload, border=0, borderwidth=0)
    reload_button.place(relx=0.061, rely=0.1, relwidth=0.03, relheight=0.8)
    change_fg_OnHover(reload_button, "yellow", "white")

    save_site_fav = tk.Button(master=nav_bar, fg='white',text="♠", font=("Arial Bold", 17),activebackground=nav_bar_bg, activeforeground='yellow' , command=save_site_fav_save , bg=nav_bar_bg , border=0, borderwidth=0)
    save_site_fav.place(relx=0.091, rely=0.1, relwidth=0.03, relheight=0.8)
    #change_fg_OnHover(save_site_fav, "yellow", "white")

    search_bar = tk.Entry(master=nav_bar, bg='#232B2B', fg='white', font=("Consolas", 12), textvariable=search_url,border=0, borderwidth=0.5)
    search_bar.place(relx=0.122, rely=0.05, relwidth=0.41, relheight=0.9)
    search_bar.bind("<Return>", button_s)
    #change_bg_OnHover(search_bar,"#362819" ,"#232B2B")
    test_search(search_bar, "#362819" ,"#232B2B")



    Home_bt = tk.Button(master=nav_bar, fg='white' ,bg=nav_bar_bg, text='⤊',  font=("Arial Bold", 18),border=0, borderwidth=0, command=Home_show_Page)
    Home_bt.place(relx=0.532, rely=0.05, relwidth=0.02, relheight=0.9)
    change_fg_OnHover(Home_bt, "yellow", "white")

    # =================== Tab Preview Section =======

    Tabs_view = tk.Frame(nav_bar, bg=nav_bar_bg)
    Tabs_view.place(relx=0.552, rely=0.05, relwidth=0.44, relheight=0.9)

    new_tab_bt = tk.Button(master=Tabs_view, fg='white',text="+", font=("Arial Bold", 13), activebackground=nav_bar_bg, activeforeground='yellow'  , bg=nav_bar_bg , command=lambda :New_Tab_New_wind("https://www.google.com"), border=0, borderwidth=0)
    new_tab_bt.pack(side=tk.LEFT,fill='y',  ipadx=4)
    change_fg_OnHover(new_tab_bt, "red", "white")


    # ==================== Setting Section ======

    setting_ = tk.Button(nav_bar, fg="white", bg=nav_bar_bg, border=0, borderwidth=0, activebackground=nav_bar_bg, text="۞", font=("Consolas", 16))
    setting_.place(relx=0.972, rely=0.05, relwidth=0.028, relheight=0.9)
    change_fg_OnHover(setting_, "red", "white")

    # =========================== Home Page=====================================================================================================================
    def resize(file_location):
        img = (Image.open(file_location))
        Resized_image = img.resize((screen_width, screen_height), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(Resized_image)
        return new_image


    img = resize("background.jpg")
    Home_Tab = tk.Label(app, border=0, bg=nav_bar_bg, image=img)
    Home_Tab.place(y=30, relwidth=1, relheight=0.977)
    home_page(Home_Tab)


    #Home_Tab = tk.Frame(app, bg=nav_bar_bg)
    #Home_Tab.place(y=30, relwidth=1, relheight=0.977)


    #Tab = WebView2(Home_Tab, 500, 500)
    #Tab.pack(fill="both", expand=True)
    #Tab.load_url('https://github.com/Hezron26')
    #top_webview = Tab



    app.after(1000, lambda :recall())
    #app.after(3000, lambda: top_webview.evaluate_js('document.title', print))


    # ================================================================================================================================================================
    #Tab.newwindow=print("new")

    app.protocol("WM_DELETE_WINDOW", Sytem_close) # bind the WM_DELETE_WINDOW protocol to the on_close function
    app.mainloop()




if __name__ == "__main__":
    t = Thread(ThreadStart(main))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()