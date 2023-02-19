import customtkinter
import tkinter as tk
customtkinter.set_appearance_mode("system")  # default value
customtkinter.deactivate_automatic_dpi_awareness()
import clr
from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime
#clr.AddReference('System')
clr.AddReference('System.Windows.Forms') # load the .NET assembly for the System.Windows.Forms namespace
clr.AddReference('System.Threading') # load the .NET assembly for the System.Threading namespace.
from System.Windows.Forms import Control
from System.Threading import Thread,ApartmentState,ThreadStart


if not have_runtime():#There is no webview2 runtime or the version is too low
    install_runtime()#Download and install runtime

count  = 1
top_webview = None
current_tabe = None
track_pair_widget = {}
track_pair_widget1 = {}


def main():
    global count
    global Visited_links
    global top_webview
    global current_tabe
    global track_pair_widget , track_pair_widget1

    def Sytem_close():
        for child in app.winfo_children():  # destroy all child widgets of a frame:
            child.destroy()  # destroy all child widgets
            # shut down Python.NET

        app.destroy()

    def get_cur_url(num):
        search_url.set(num.get_url())

    def Go_back():
            top_webview.web.GoBack()

    def Go_Forwad():
            top_webview.web.GoForward()


    def button_event():
        print("1",Tab.get_url())
        print("2",Tab.web_view.get_current_url())
        Tab.chwnd
        print(Tab.newwindow)
        pass

    def reload():
        top_webview.reload()

    def button_s(num):
        global top_webview
        print(search_url.get())
        top_webview.load_url(url=f'https://{search_url.get()}')

        while not top_webview.loaded:
            print(12)
            pass
        print('Page Loaded', top_webview.get_url())

    def frame_changer(frame):
        frame.tkraise()

    def change_bg_OnHover(button, colorOnHover, colorOnLeave):  # Color change on Mouse Hover
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

    def change_fg_OnHover(button, colorOnHover, colorOnLeave):  # Color change on Mouse Hover
        button.bind("<Enter>", func=lambda e: button.config(fg=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(fg= colorOnLeave))

    def site_info():
       print(Tab.loaded)

    def Home_Page():
        Home_Tab.tkraise()

    def New_Tab_New_wind():
        global count
        global top_webview
        global current_tabe
        global track_pair_widget, track_pair_widget1

        if track_pair_widget != {}:
            for x in track_pair_widget:
               track_pair_widget[x].configure(bg='#1C352D')

            for x in track_pair_widget1:
                   track_pair_widget1[x].configure(bg='#1C352D')




        def close_tab(t_num, w_num):
            for child in t_num.winfo_children(): #  destroy all child widgets of a frame:
                child.destroy()  #  destroy all child widgets
            for child in w_num.winfo_children(): #  destroy all child widgets of a frame:
                child.destroy() #  destroy all child widgets
            t_num.destroy() #  destroy all frame widgets
            w_num.destroy() #  destroy all frame widgets

            track_pair_widget.pop(w_num)  #  Remove  widgets
            track_pair_widget1.pop(w_num) #  Remove  widgets


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
        new_web_view.load_url('https://youtube.com')
        top_webview = new_web_view

        # ========================  Creating a new tab in the Tabs preview ==========

        new_tab_wid = tk.Frame(Tabs_view, bg='#232B2B')
        new_tab_wid.pack(side=tk.LEFT, fill='y', ipadx=60)
        change_bg_OnHover(new_tab_wid, 'yellow', '#232B2B')

        fr = tk.Frame(new_tab_wid, bg='gray')
        fr.place(relx=0.02, rely=0.02, relheight=0.98, relwidth=0.96)

        disp_tab = tk.Button(fr, text=f"{count}", bg='#8A9A5B', anchor="w",borderwidth=0, border=0, activebackground="#27251F", activeforeground="white", )
        disp_tab.place(relheight=1, relwidth=0.8, relx=0)
        current_tabe = disp_tab
        disp_tab.configure(command=lambda:Push_top(new_web_view_frame, new_web_view, current_tabe))

        track_pair_widget[new_web_view_frame] = disp_tab

        close_bt = tk.Button(fr, text="X", bg='#8A9A5B', activebackground='gray', activeforeground='red', borderwidth=0, border=0, font=("Consolas Bold", 11), command=lambda:close_tab(new_tab_wid,new_web_view_frame))
        close_bt.place(relheight=1, relwidth=0.2, relx=0.8)
        track_pair_widget1[new_web_view_frame] = close_bt

        count +=1




        # ====


    app = tk.Tk()
    app.geometry("600x500")
    app.title("Hezron Browser")
    #app.configure(fg_color='gold')
    app.iconbitmap("panda.ico")
    #app.iconphoto(False, tk.PhotoImage(file='panda.jpg'))
    #app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file='mut.png'))
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

    site_info_button = tk.Button(master=nav_bar, fg='white',text="♠", font=("Arial Bold", 17),activebackground=nav_bar_bg, activeforeground='yellow'  , bg=nav_bar_bg , command=site_info, border=0, borderwidth=0)
    site_info_button.place(relx=0.091, rely=0.1, relwidth=0.03, relheight=0.8)
    change_fg_OnHover(site_info_button, "yellow", "white")

    search_bar = tk.Entry(master=nav_bar, bg='#232B2B', fg='white', font=("Consolas", 12), textvariable=search_url,border=0, borderwidth=0.5)
    search_bar.place(relx=0.122, rely=0.05, relwidth=0.41, relheight=0.9)
    search_bar.bind("<Return>", button_s)
    change_bg_OnHover(search_bar,"#362819" ,"#232B2B")

    Home_bt = tk.Button(master=nav_bar, fg='white' ,bg=nav_bar_bg, text='⤊',  font=("Arial Bold", 18),border=0, borderwidth=0, command=Home_Page)
    Home_bt.place(relx=0.532, rely=0.05, relwidth=0.02, relheight=0.9)
    change_fg_OnHover(Home_bt, "yellow", "white")

    # =================== Tab Preview Section =======

    Tabs_view = tk.Frame(nav_bar, bg=nav_bar_bg)
    Tabs_view.place(relx=0.552, rely=0.05, relwidth=0.44, relheight=0.9)

    new_tab_bt = tk.Button(master=Tabs_view, fg='white',text="+", font=("Arial Bold", 13), activebackground=nav_bar_bg, activeforeground='yellow'  , bg=nav_bar_bg , command=New_Tab_New_wind, border=0, borderwidth=0)
    new_tab_bt.pack(side=tk.LEFT,fill='y',  ipadx=4)
    change_fg_OnHover(new_tab_bt, "red", "white")


    # ==================== Setting Section ======

    setting_ = tk.Button(nav_bar, fg="white", bg=nav_bar_bg, border=0, borderwidth=0, activebackground=nav_bar_bg, text="۞", font=("Consolas", 16))
    setting_.place(relx=0.972, rely=0.05, relwidth=0.028, relheight=0.9)
    change_fg_OnHover(setting_, "red", "white")

    # =========================== Home Page=====================================================================================================================
    Home_Tab = tk.Frame(app, bg=nav_bar_bg)
    Home_Tab.place(y=30, relwidth=1, relheight=0.977)

    Tab = WebView2(Home_Tab, 500, 500)
    Tab.pack(fill="both", expand=True)
    Tab.load_url('https://github.com/Hezron26')
    top_webview = Tab

    get_cur_url(Tab)
    # ================================================================================================================================================================


    app.protocol("WM_DELETE_WINDOW", Sytem_close) # bind the WM_DELETE_WINDOW protocol to the on_close function
    app.mainloop()




if __name__ == "__main__":
    t = Thread(ThreadStart(main))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()