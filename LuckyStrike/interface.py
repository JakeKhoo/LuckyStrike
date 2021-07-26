from tkinter import *
from Orbit import *
from tkinter import messagebox
from functools import partial
from random import *
import pygame

def login():
    global username
    global password

    def add_account(user, passw):
        test_query = "SELECT * FROM accounts WHERE username = '%s' "%(user.get())
        results = readQuery(connection,test_query)
        if len(results) == 0 :
                sql_query = "INSERT INTO accounts VALUES ('%s', '%s','%d','%d','%d')"%(user.get(),passw.get(),0,0,0)
                executeQuery(connection, sql_query)
                return messagebox.showinfo(title="Success",message="registration Successful")
                
        else:
                return messagebox.showerror(title="Error",message="Username in use!")



    def validate_login(user, passw,window):
            validate_query = "SELECT * FROM accounts WHERE username = '%s' AND password = '%s' "%(user.get(),passw.get())
            results = readQuery(connection,validate_query)
            if len(results) == 0 or  user.get()== "" :
                    return messagebox.showerror(title="Error",message="Wrong username/password !")
            else:
               window.destroy()
               homepage()

    
    #window
    login_window = Tk()  
    login_window.geometry('400x400')  
    login_window.title('LuckyStrike')
   

    #background
    img = PhotoImage(file="Untitled.png")
    label = Label(
        login_window,
        image=img
    )
    label.place(x=0, y=0)

    #username label and text entry box
    usernameLabel = Label(login_window, text="Username",fg="white",bg="purple")
    usernameLabel.place(x=100,y=200)
    username = StringVar()
    usernameEntry = Entry(login_window, textvariable=username)
    usernameEntry.place(x=170,y=200)

    #password label and password entry box
    passwordLabel = Label(login_window,text="Password",fg="white",bg="purple")
    passwordLabel.place(x=100,y=225)
    password = StringVar()
    passwordEntry = Entry(login_window, textvariable=password, show='*')
    passwordEntry.place(x=170,y=225)

    #validate login and account creation
    validatelogin = partial(validate_login, username, password,login_window)
    addaccount = partial(add_account,username,password)

    #login button
    loginButton = Button(login_window, text="Login", command=validatelogin, fg ="white",bg="green")
    loginButton.place(x =150,y=250)

    #register button
    registerButton = Button(login_window, text="Register", command=addaccount, fg ="white",bg="green")
    registerButton.place(x=250,y=250)
    
    login_window.mainloop()

def sized(button):
    button.config(height = 2, width = 18)

def get_credit():
    coins_query = "SELECT credit FROM accounts WHERE username = '%s'"%(username.get())
    credit = readQuery(connection, coins_query)[0][0]
    return credit

def homepage():
    #window
    global home_window
    home_window = Tk()
    home_window.geometry('400x400')  
    home_window.title('LuckyStrike')
    home_window.configure(background = "white")
    

    #Number of coins
    img = PhotoImage(file="coin3.png")
    label_coin = Label(
        home_window,
        image=img, bg = "white"
    )
    label_coin.place(x=-80, y=-40)
    coins_query = "SELECT credit FROM accounts WHERE username = '%s'"%(username.get())
    credit = readQuery(connection, coins_query)[0][0]
    
    label4 = Label(home_window, text = "x"+ str(credit), fg="black", bg ="white")
    label4.place(x=45,y=44)
    #Username
    label1 = Label(home_window, text="Hello there,  " + username.get(), fg="black", bg="white")
    label1.place(x=3, y=5)


    #Connect to server
    ConnectionButton = Button(home_window, text="Information", command=None, fg ="white",bg="green")
    ConnectionButton.place(x =235,y=20)
    sized(ConnectionButton)

    #Click to play button
    PlayButton = Button(home_window, text="Click To Play", command=run, fg ="white",bg="purple")
    PlayButton.place(x=235,y=120)
    sized(PlayButton)

    #Top up button
    TopupButton = Button(home_window, text="Top-up Coins", command=topup, fg ="white",bg="green")
    TopupButton.place(x =235,y=220)
    sized(TopupButton)

    #Check Prizes button
    PrizesButton = Button(home_window, text="Check Prizes", command=checkprizes, fg ="white",bg="purple")
    PrizesButton.place(x=235,y=320)
    sized(PrizesButton)

    #Log out button
    def logout():
        home_window.destroy()
        login()
    LogOutButton = Button(home_window, text="Logout", command=logout, fg ="white",bg="red")
    LogOutButton.place(x=30,y=320)
    sized(LogOutButton)
    home_window.mainloop()

def topup():
    home_window.destroy()
    topup_window = Tk()
    topup_window.geometry('400x400')  
    topup_window.title('LuckyStrike')

  
    topup_window.configure(background = "white")


     

  
  
    def set_coins(x):
        setquery = "UPDATE accounts SET credit = %d WHERE username = '%s'"%(x,username.get())
        executeQuery(connection, setquery)

    def setcoins1():
        return set_coins(1+get_credit())
    def setcoins5():
        return set_coins(5+get_credit())
    def setcoins10():
        return set_coins(10+get_credit())
        


    #$1
    Button1 = Button(topup_window, text="$1 = 1 coin", command=setcoins1, fg ="white",bg="green")
    Button1.place(x =130,y=20)
    sized(Button1)

    #Click to play button
    Button5 = Button(topup_window, text="$4 = 5 coins", command=setcoins5, fg ="white",bg="purple")
    Button5.place(x =130,y=120)
    sized(Button5)


    #Top up button
    Button10 = Button(topup_window, text="$7 = 10 coins", command=setcoins10, fg ="white",bg="green")
    Button10.place(x =130,y=220)
    sized(Button10)

    #Go back
    def back():
        topup_window.destroy()
        homepage()
    BackButton = Button(topup_window, text="Back", command=back, fg ="white",bg="blue")
    BackButton.place(x=130,y=320)
    sized(BackButton)



    
    topup_window.mainloop()
def check_prizes():
    prize_query = "SELECT small_prize,big_prize FROM accounts WHERE username = '%s'"%(username.get())
    prize = readQuery(connection, prize_query)[0]
    return prize
    

def checkprizes():
    home_window.destroy()
    prizes_window = Tk()
    prizes_window.geometry('400x400')  
    prizes_window.title('LuckyStrike')

    img = PhotoImage(file="Prizes.png")
    label = Label(
        prizes_window,
        image=img
    )
    label.place(x=0, y=0)
##    img = PhotoImage(file="Prizes.png")
##    label = Label(
##        prizes_window,
##        image=img
##    )
##    label.place(x=-130, y=320)

    



    small_prize = check_prizes()[0]
    big_prize = check_prizes()[1]
    label1 = Label(prizes_window, text="x"+str(small_prize), fg="black", bg="white", font = ("Arial",25))
    label1.place(x=320, y=70)
    label2 = Label(prizes_window, text="x"+str(big_prize), fg="black", bg="white", font = ("Arial",25))
    label2.place(x=260, y=180)


    #background


##
##    #Go back
    def back():
        prizes_window.destroy()
        homepage()
    BackButton = Button(prizes_window, text="Back", command=back, fg ="white",bg="blue")
    BackButton.place(x=130,y=320)
    sized(BackButton)

    prizes_window.mainloop()

green = (0,255,0)
blue = (0,0,255)

def display(im):
    window = Tk()
    window.geometry('400x400')
    window.title('LuckyStrike')
   

    #background
    img = PhotoImage(file=im)
    label = Label(
        window,
        image=img
    )
    label.place(x=0, y=0)

    window.after(2000,lambda:window.destroy())
    window.mainloop()

def get_w(prize):
    if prize == 'big':
        x = check_prizes()[1]
        setquery = "Update accounts SET big_prize = %d WHERE username = '%s'"%(x+1,username.get())
        executeQuery(connection, setquery)
    if prize == 'small':
        y = check_prizes()[0]
        setquery = "Update accounts SET small_prize = %d WHERE username = '%s'"%(y+1,username.get())
        executeQuery(connection, setquery)



class Player(pygame.sprite.Sprite):
    def __init__(self,im):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(im).convert_alpha()
        self.clean=self.image.copy()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (188, 350)
        

    def update(self,speed,forward):
        self.rect.y += -speed
        self.rect.x += forward
    def stop(self,y):
        self.rect.y=y
    def rotate(self,angle):
        self.image = pygame.transform.rotozoom(self.clean,angle,1)
        self.rect=self.image.get_rect(center = self.rect.center)
    def set(self,x,y):
        self.rect.center = (x,y)

    def small(self):
        if self.rect.y>= 86 and self.rect.y<= 114:
            get_w('small')
            pygame.quit()
            display("Game On (1).png")

                     
    def big(self):
        if self.rect.y<=23 and self.rect.y>=18:
            get_w('big')
            pygame.quit()
            display("Game On.png")
    def no(self):
        if self.rect.y>23 and self.rect.y<86 or self.rect.y<18 or self.rect.y>114:
            pygame.quit()
            display("Game On (2).png")

class win(pygame.sprite.Sprite):
    def __init__(self,length,height,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,length))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (397, height)
 


def run():
    no_credit = False
    coins = readQuery(connection,"SELECT credit FROM accounts WHERE username = '%s'"%(username.get()))[0][0]
    if coins <= 0:
        messagebox.showerror(title="Error",message="Insufficient coins!")
        no_credit = True
    else:
        executeQuery(connection,"Update accounts SET credit = %d WHERE username = '%s'"%(coins-1,username.get()))
        home_window.destroy()
       




    
    pygame.init()
    screen = pygame.display.set_mode([400, 400])
    running = True
    bg = pygame.image.load("Untitled design (1).png").convert()
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    rate = 4.97+random()/5
    player = Player("Mini_Truck.png")
    player2 = Player("Mini_Truck - Copy.png")
    big = win(28,35,green)
    small = win(50,115,blue)

    all_sprites.add(player)
    all_sprites.add(big)
    all_sprites.add(small)

    angle = 0


    speed = randrange(1,10)
    stop = True
    move = True
    stop2 = True
    


    while running and not no_credit:
        clock.tick(30)
        
      

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    location = player.rect.y

                    player.stop(location)
                    all_sprites.update(0,0)
                    stop =False
            if event.type == pygame.MOUSEBUTTONUP:

                    location = player.rect.y

                    player.stop(location)
                    all_sprites.update(0,0)
                    stop =False  
                
                    
        if stop == True:
            
            all_sprites.update(rate,0)

        if stop == False and angle!=-92:
            angle-=4
            player.rotate(angle)
        if angle == -92:
            y = player.rect.y
            x = player.rect.x
            player2.set(x+38,y+18)
            player.rect.y=500
            all_sprites.add(player2)
            angle-=1
            move = False
        if move == False and stop2 == True:
            player2.update(0,4)
        if player2.rect.x > 330:
            stop2 = False
        if stop2 == False:
            player2.update(0,0)
            player2.small()
            player2.big()
            player2.no()



            break
            

            
            
            
            
            

            



            
        if player.rect.y<=-60:
            running = False
            player2.no()
            
        # Fill the background with white
        else:
            screen.blit(bg, [0, 0])
    ##    screen.blit(player.image,player.rect)
            all_sprites.draw(screen)
        # *after* drawing everything, flip the display

            pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
    if no_credit==False:
        

        homepage()
 


login()




