import customtkinter
import ctypes
import mysql.connector
import datetime
import uuid

def get_hwid():
    hwid = uuid.getnode()
    hwid_str = format(hwid, 'x')
    return hwid_str

def main_gui():
    customtkinter.set_appearance_mode("dark")  
    customtkinter.set_default_color_theme("blue") 

    app = customtkinter.CTk()
    app.geometry("800x600")
    app.title("Hello there! Your in.")

    
    label = customtkinter.CTkLabel(master=app, text="Your main gui here")
    label.grid(row=0, column=1, pady=10, padx=10)

    app.mainloop()

def check_license_from_database(license_key):
    try:
        db_connection = mysql.connector.connect(
            host="",
            user="",  
            password="", 
            database=""  
        )
        if db_connection.is_connected():
            cursor = db_connection.cursor()
            cursor.execute("SELECT * FROM `licences` WHERE `license` = '" + license_key + "'")
            results = cursor.fetchall()
            if(results):
                cursorfetchone = results[0]
                hwid = cursorfetchone[2]
                enddate = cursorfetchone[3]
                if(get_hwid() != hwid):
                    if(hwid == 'none'):
                        cursor.execute("UPDATE `licences` SET `hwid` = '" + get_hwid() + "' WHERE `license` = '" + license_key + "'")
                        db_connection.commit()
                        return True
                    ctypes.windll.user32.MessageBoxW(0, "Your HWID does not match the license HWID. Please contact support.", "Error", 0)
                    return False
                else:
                    if(datetime.datetime.now() > enddate):
                        ctypes.windll.user32.MessageBoxW(0, "Your license has expired. ", "Error", 0)
                        return False
                    else:
                        return True
            else:
                return False

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()

def license_gui():
    app = customtkinter.CTk()
    app.geometry("800x600")
    app.title("Enter Your License")
    customtkinter.set_appearance_mode("dark")  
    customtkinter.set_default_color_theme("blue") 
    label_license = customtkinter.CTkLabel(master=app, text="Enter Your License:")
    label_license.pack(pady=10)

    entry_license = customtkinter.CTkEntry(master=app, width=350)
    entry_license.pack(pady=10)
    def check_license_callback():
        license_key = entry_license.get()
        if check_license_from_database(license_key):
            app.destroy()
            main_gui()
        else:
            ctypes.windll.user32.MessageBoxW(0, "You entered the wrong license key", "Error", 0)

    button_check_license = customtkinter.CTkButton(master=app, text="Check", command=check_license_callback)
    button_check_license.pack(pady=10)

    app.mainloop()

license_gui()