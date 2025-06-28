from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SERVER MENU</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" integrity="sha512-YWzhKL2whUzgiheMoBFwW8CKV4qpHQAEuvilg9FAn5VJUDwKZZxkJNuGM4XkWuk94WCrrwslk8yWNGmY1EduTA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
   <link rel="stylesheet" href="style.css" type="text/css" media="all" />
    <style>
        *{

    box-sizing: border-box;

    margin: 0;
    padding: 0;
}
body {
    font-family: "Poppins", sans-serif;
    --color1: #FFF ;
    --color2: #181818 ;
    background-color: white;
    background-size: cover;
    color: white;
}
h3{
    font-size: 12px;
    color: black;
    text-align: center;
}
h2{
    text-align: center;
    font-size: 19px;
    font-family: cursive;
    color: black;
}
.nav-bar {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    list-style: none;
    position: relative;
    background-color: var(--color2);
    padding: 12px 20px;
}
.logo img {width: 40px;}
.menu {display: flex;}
.menu li {padding-left: 30px;}
.menu li a {
    display: inline-block;
    text-decoration: none;
    color: var(--color1);
    text-align: center;
    transition: 0.15s ease-in-out;
    position: relative;
    text-transform: uppercase;
}
.menu li a::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 1px;
    background-color: var(--color1);
    transition: 0.15s ease-in-out;
}
.menu li a:hover:after {width: 100%;}
.open-menu , .close-menu {
    position: absolute;
    color: var(--color1);
    cursor: pointer;
    font-size: 1.5rem;
    display: none;
}
.open-menu {
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
}
.close-menu {
    top: 20px;
    right: 20px;
}
#check {display: none;}
@media(max-width: 610px){
    .menu {
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 80%;
        height: 100vh;
        position: fixed;
        top: 0;
        right: -100%;
        z-index: 100;
        background-color: var(--color2);
        transition: all 0.2s ease-in-out;
    }
    .menu li {margin-top: 40px;}
    .menu li a {padding: 10px;}
    .open-menu , .close-menu {display: block;}
    #check:checked ~ .menu {left: 0;}
}

.convo{
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
    width: 250px;
    height: 120px;
    background-color: #707070;
    margin-left: 55px;
}
h1{
    margin-top: 10px;
    color: black;
    font-size: 12px;
    text-align: center;
}

details{
    color: red;
}
.image-container {
  position: relative;
  width: 330px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.imager-containe{

  position: relative;


  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 2px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-container {
  position: relative;
  width: 330px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-container {
  position: relative;
  width: 330px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}

.image-containe{
  position: relative;

  width: 300px; /* adjust the width to your image size */
  height: 200px; /* adjust the height to your image size */
  margin: 13px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.image{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;
}
.button-34 {
  background: black;
  border-radius: 999px;
  box-shadow: black 0 10px 20px -10px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  font-family: Inter,Helvetica,"Apple Color Emoji","Segoe UI Emoji",NotoColorEmoji,"Noto Color Emoji","Segoe UI Symbol","Android Emoji",EmojiSymbols,-apple-system,system-ui,"Segoe UI",Roboto,"Helvetica Neue","Noto Sans",sans-serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 24px;
  opacity: 1;
  outline: 0 solid transparent;
  padding: 8px 18px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  width: fit-content;
  word-break: break-word;
  border: 0;
  margin-bottom:12px;
}

.footer {
    text-align: center;
    margin-top: 10px;
    color: black;
}
h4{
    color: white;
    font-family: bold;
    text-align: center;
}
    </style>
    </head>
    
<body>
    <header>
    <nav>
        <ul class='nav-bar'>
            <div class="text-2xl text-primary">𝐌𝐀𝐃𝐄 𝐁𝐘 𝐓𝐇𝐄 𝐋𝐄𝐆𝐄𝐍𝐃 𝐍𝐈𝐓𝐄𝐒𝐇♚</div>
            <input type='checkbox' id='check' />
            <span class="menu">
                <li><a href="https://wa.me/+9779800640944">Contact:)</a ></li>
                                                
                </li>
                <label for="check" class="close-menu"><i class="fas fa-times"></i></label>
            </span>
            <label for="check" class="open-menu"><i class="fas fa-bars"></i></label>
        </ul>
    </nav>
    </header>
    <br />
    <h2>WEB SERVER OWNER ➤ NITESH XD</h2>
    <br />
    <div class="image-container">
  <img src="https://i.ibb.co/bgVJV53s/Picsart-25-05-04-14-16-34-846.jpg" alt="Image" class="image">
   <h1>➤Convo Tool꧂</h1>
<br />
<button class="button-34" role="button" onclick="window.location.href='http://de1.bot-hosting.net:22787'">⊲ CONTACT ⊳</button>
    <br />
    <br />
        <div class="image-containe">
 <img src="https://i.ibb.co/TMmDwf3n/Picsart-25-03-26-01-24-55-663.jpg" alt="Image" class="image">
 <h1>➤ MULTY TOKEN + SINGLE TOKEN CONVO SERVER FOR INBOX/GROUP CHAT CLICK ON CHECK BUTTON FOR USING THIS TOOL꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://nites-567x.onrender.com//'">⊲ CHECK ⊳</button>
    <br />
    <br />
            <div class="imager">
 <img src="https://i.ibb.co/MyvMn6gy/Picsart-25-01-01-19-26-53-901.jpg" alt="Image" class="image">
 <h1>➤ SINGLE TOKEN CONVO SERVER WITH LOG METHOD FOR INBOX/GROUP CHAT CLICK ON CHECK BUTTON FOR USING THIS TOOL꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://nitesh-bwhv.onrender.com/'">⊲ CHECK ⊳</button>
    <br />
    <br />
            <div class="imager">
 <img src="https://i.ibb.co/9HYdHDGS/5963a5a33096170f57a8da790612076e.jpg" alt="Image" class="image">
    <h1>➤ MULTY POST LOADER PAGE ID + SIMPLE ID + ANTHER IDZ COOKIES SERVER CLICK ON CHECK BUTTON FOR USING THIS TOOL꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='http://405715.site.bot-hosting.net/server'">⊲ CHECK ⊳</button>
    <br />
    <br />
            <div class="imager">
 <img src="https://i.ibb.co/sJKN5FG5/535f86f072002b29eea5135cd7a8a66e.jpg" alt="Image" class="image">
 <h1>➤ GC NAME LOCKED꧂ </h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='http://104.168.76.139:27009/'">⊲ CHECK ⊳</button>
    <br />
    <br />
           <div class="imager">
 <img src="https://i.ibb.co/PZxHSVXR/4b2e2d8f306a62e55f95555ab95fc4f6.jpg" alt="Image" class="image">
 <h1>➤ TOKEN CHECKER TOOL FOR CHECKING YOUR TOKEN IS VALID OR INVAILD CLICK ON CHECK BUTTON FOR USING THIS TOOL꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='http://fi5.bot-hosting.net:20136/'">⊲ CHECK ⊳</button>
    <br />
    <br />
          <div class="imager">
 <img src="https://i.ibb.co/xSKH7yFm/94fda4ae9ea78c88d858589a119f0294.jpg" alt="Image" class="image">
 <h1>➤ Gc Uid Page extracter꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://pagetoken.darkester.online'">⊲ CHECK ⊳</button>
    <br />
    <br />
          <div class="imager">
 <img src="https://i.ibb.co/RTbMZ9Q7/9d919c3914f1feab7904e9a9c68f433d.jpg" alt="Image" class="image">
     <h1>➤ Token Generater꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://generator.darkester.online'">⊲ CHECK ⊳</button>
    <br />
    <br />
          <div class="imager">
 <img src="https://imagesaver.darkester.online/uploads/1750970878-1000036627.jpg" alt="Image" class="image">
 <h1>➤ WHATAPP OFFLINE SERVER @ɴɪᴛᴇꜱʜ 2024꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://wp-offline-server.onrender.com'">⊲ CHECK ⊳</button>
    <br />
    <br />
          <div class="imager">
 <img src="https://imagesaver.darkester.online/uploads/1750971336-1000008940.jpg" alt="Image" class="image">
     <h1>➤WhatsApp Cred.json Generator꧂</h1>
 <br />
 <button class="button-34" role="button" onclick="window.location.href='https://creds-6mgr.onrender.com'">⊲ CHECK ⊳</button>
    <br />
    <br />
       <div class="imager">
 <img src="https://i.ibb.co/Y7HVjJsd/1398bde80ec98869c30b06001e376d76.jpg" alt="Image" class="image">
 <h1>➤ ALL WEB TO WEB TOOLS + ALL TERMUX TOOL꧂</h1>
 <br />
    <br />
    
    <div class="footer">
    <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
      <div class="mb-4 md:mb-0">
        <a href="/terms" class="hover:text-primary">Terms</a>
        <span class="mx-2">|</span>
        <a href="/privacy" class="hover:text-primary">Privacy</a>
      </div>
      
      <div id="links" class="flex space-x-4">
        <a href="https:/https://www.facebook.com/NiteshFaadbazz" class="text-2xl hover:text-primary"><i class="fab fa-facebook"></i></a>
        <a href="https://wa.me/+9779800640944" class="text-2xl hover:text-primary"><i class="fab fa-whatsapp"></i></a>
        <a href="https://github.com/HassanRajput0/" class="text-2xl hover:text-primary"><i class="fab fa-github"></i></a>
      </div>
      
      <div class="mt-4 md:mt-0 text-center">
        <p>© 2024 Nitesh master. All Rights Reserved.</p>
        <p>Made with ❤️ by <a href="">NITESH ONIK</a></p>
      </div>
        <br />
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
