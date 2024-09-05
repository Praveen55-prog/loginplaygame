from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL
import random
app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Praveen55"
app.config["MYSQL_DB"]="login"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

@app.route("/")
def sig():
    return render_template("signin.html")   

@app.route('/signin' ,methods=["POST","GET"])
def signin():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        con=mysql.connection.cursor()
        sql="insert into signin (username,password) value(%s,%s)"
        con.execute(sql,(username,password))
        mysql.connection.commit()
        con.close()
        return render_template("login.html")

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        con=mysql.connection.cursor()
        sql="select * from signin where username=%s and password=%s"
        con.execute(sql,(username,password))
        user=con.fetchone()
        con.close()

        if user:
            return render_template("welcome.html")
        else:
            return render_template("signin.html")
    


   
@app.route("/flames",methods=["POST","GET"])    
def flames():  
    if request.method=="POST":      
        a=request.form.get('name')
        b=request.form.get('par')
        c=[x for sub in a for x in sub]
        d=[x for sub in b for x in sub]   
        e=[]
        for i in c:
            if i in d:
                d.remove(i)
            else:
                e.append(i)
        e.extend(d)      
        e=len(e)
        f=["f","l","a","m","e","s"]      
        f1=f*e
        for i in range(6):
            v=f1[e-1]
            if v in f1[0]:
                for i in f1:
                    if i==v:
                        f1.remove(v)
            elif v in f1[5]:
                for i in f1:
                    if i==v:
                        f1.remove(v)
            elif v in f1[1]:   
                for i in f1:
                    if i==v:
                        f1.remove(v)     
                for i in range(1):
                    f1.append(f1[0]) 
                    f1.remove(f1[0])
            elif v in f1[2]:
                for i in f1:
                    if i==v:
                        f1.remove(v)     
                for i in range(2):
                    f1.append(f1[0]) 
                    f1.remove(f1[0])    

            elif v in f1[3]:
                for i in f1:
                    if i==v:
                        f1.remove(v)     
                for i in range(3):
                    f1.append(f1[0]) 
                    f1.remove(f1[0]) 
            elif v in f1[4]:
                for i in f1:
                    if i==v:
                        f1.remove(v)     
                for i in range(4):
                    f1.append(f1[0]) 
                    f1.remove(f1[0])   
        if "f" in f1:
            F="You Boht are Friends"
            c=F
        elif "l" in f1:
            L="Lovers"
            c=L
        elif "a" in f1:
            A="Affectionate"     
            c=A
        elif "m" in f1:
            M="Marriage"   
            c=M
        elif "e" in f1:
            E="Enemy"
            c=E
        elif "s" in f1:
            S="Siblings"  
            c=S  
        return render_template("flames.html" ,a=a.upper(), b=b.upper() ,c=c)     

@app.route('/flames1')
def flames1():
    return render_template("flames.html")

@app.route('/log')
def log():
    return render_template("login.html")
@app.route('/stonepaperscissor')  
def stonepaperscissor():
    return render_template("stone.html")
@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")
@app.route('/stone',methods=["POST","GET"])
def stone():
    if request.method=="POST":
        c=request.form["name"]
        a1=["stone","paper","scissors"]
        user=["You Clicked Stone","You Clicked Paper","You Clicked Scissors"]
    
        for i in range(len(a1)):
            if c ==a1[i]:
                c=user[i]
                b=random.choice(a1)
                b1="Computer Selected"+" "+b
                if c=="You Clicked Stone":
                    if b=="scissors":
                        y="You won the Game"
                        con=mysql.connection.cursor()
                        sql="update score set points=points+1 where names=1"
                        con.execute(sql)
                        mysql.connection.commit()
                    elif b=="stone":
                        y="Match Draw"
                    else:
                        y="Computer won the Game"
                        con=mysql.connection.cursor()
                        sql="update score set points=points+1 where names=2"
                        con.execute(sql)
                        mysql.connection.commit()                            
                    con=mysql.connection.cursor()
                    sql="select * from score where names=1"
                    con.execute(sql)
                    resultu=con.fetchone()
                    pointsu=resultu['points']
                    sql="select * from score where names=2"
                    con.execute(sql)
                    resultc=con.fetchone()
                    pointsc=resultc['points']
                    if pointsc==5:
                        con=mysql.connection.cursor()
                        sql="update score set points=0 where names=2"
                        con.execute(sql)
                        sql="update score set points=0 where names=1"
                        con.execute(sql)
                        mysql.connection.commit()
                        cw="Computer Won the Game"
                        
                        return render_template("stone.html",c=c,b1=b1,y=y,pointsc=pointsc,pointsu=pointsu,cw=cw)
                    if pointsu==5:
                        con=mysql.connection.cursor()
                        sql="update score set points=0 where names=1"
                        con.execute(sql)
                        sql="update score set points=0 where names=2"
                        con.execute(sql)
                        mysql.connection.commit()
                        uw="You Won the Game"
                        
                        return render_template("stone.html",c=c,b1=b1,y=y,pointsc=pointsc,pointsu=pointsu,uw=uw)                     


                    return render_template("stone.html",c=c,b1=b1,y=y,pointsc=pointsc,pointsu=pointsu)
                elif c=="You Clicked Paper":
                    if b=="stone":
                        y="You won the Game"
                        con=mysql.connection.cursor()
                        sql="update score set points=points+1 where names=1"
                        con.execute(sql)
                        mysql.connection.commit()
                    elif b=="paper":
                        y="Match Draw"
                    else:
                        y="Computer won the Game"
                        con=mysql.connection.cursor()
                        sql="update score set points=points+1 where names=2"
                        con.execute(sql)
                        mysql.connection.commit()                            
                    con=mysql.connection.cursor()
                    sql="select * from score where names=1"
                    con.execute(sql)
                    resultu=con.fetchone()
                    pointsu=resultu['points']
                    sql="select * from score where names=2"
                    con.execute(sql)
                    resultc=con.fetchone()
                    pointsc=resultc['points']
                    if pointsc==5:
                        con=mysql.connection.cursor()
                        sql="update score set points=0 where names=2"
                        con.execute(sql)
                        sql="update score set points=0 where names=1"
                        con.execute(sql)
                        mysql.connection.commit()
                        cw="Computer Won the Game"  
                        
                        return render_template("stone.html",c=c,b1=b1,y=y,pointsc=pointsc,pointsu=pointsu,cw=cw)
                    if pointsu==5:
                        con=mysql.connection.cursor()
                        sql="update score set points=0 where names=1"
                        con.execute(sql)
                        sql="update score set points=0 where names=2"
                        con.execute(sql)
                        mysql.connection.commit()
                        uw="You Won the Game"
                        
                        return render_template("stone.html",c=c,b1=b1,y=y,pointsc=pointsc,pointsu=pointsu,uw=uw)
                        
                    return render_template("stone.html",c=c,b1=b1,y=y,pointsc=pointsc,pointsu=pointsu)
                    
                elif c=="You Clicked Scissors":
                    
                    if b=="paper":
                        y="You won the Game"
                    elif b=="scissors":
                        y="Match Draw"
                    else:
                        y="Computer won the Game"
                    return render_template("stone.html",c=c,b1=b1,y=y)                    
    
    else:
        return render_template("stone.html")

@app.route('/computer')
def computer():
    a1=["stone","paper","scissors"]
    b1=random.choice(a1)
    return render_template("stone.html",b1=b1)
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


if __name__=="__main__":     
    app.run(debug=True)     