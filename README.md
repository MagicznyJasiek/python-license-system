# Python license system 
## How to use?
You need to have python installed, once that is done you need to run main.py file with python.
For the script to work, you need to provide valid database data into your code. This can be found around line 30 of the code.

## How to store database data?
You need to store database data in this format no matter what. Otherwise, the script won't work.
- ID (A_I) (int)
- license (Your main license key) (text)
- hwid (user's hwid, once license is created can be set to 'none' - it will auto update itself) (text)
- enddate (end date of the license, when is license due.) (datetime)
  
Example of proper database:
![image](https://github.com/MagicznyJasiek/python-license-system/assets/61098959/e42fb6f5-8f99-4863-aadc-283524e997dd)

## How to add my normal script to this?
To add your normal script, you need to add it to the **main_gui** function. Once the valid license is provided, this function is triggered.

## Packages to install:

customtkinter, mysql.connector. You can install them by using those two commands:
```
pip install customtkinter
pip install mysql.connector
```


## Common errors:

> When I click check, the window is frozen and nothing happens.
You probably entered the database information wrong. See valid database storing or check your database data.
> When my license is valid, the gui disappears and nothing happens.
Once the script detects a good license, the **main_gui** function is triggered. Check if you have anything in this function as this is your main script code.
