import requests
import time

TITLE = """
                 ------------------------------------
                 --         Sub Domain Finder      --
                 --                 By             --
                 --           @Mr_Amir_Typer       --
                 --                                --
                 ------------------------------------
                 """
print(TITLE)

td = input("[*] Site = ")
    
a = requests.get ("https://api.hackertarget.com/hostsearch/?q="+td)

if td:
   
    print('''

[*] SubDomains:

    ''')
    print(a.text)
    time.sleep(8)
else:
    print('''

[*] Something Happend!! [ Error ] '''

          )
    
# for end
    
print("""

[Bye Friend <3 | Script By @Mr_Amir_Typer]

    """)
