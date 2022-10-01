import os

from flask import Flask, render_template, request, flash, redirect, session, url_for
from Database import Data
import mysql.connector
from MyKNeighborsClassifier import KNNeighbors

app = Flask(__name__)
app.secret_key = 'SECRET KEY'


# @app.route('/', methods=["GET", "POST"])
# def index():
#
#
#      return render_template("main.html")

@app.route('/', methods=["GET","POST"])
def index():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cancerprediction"
    )
    mycursor = mydb.cursor()
    if request.method == 'POST':
        mean_radius = request.form['mean_radius']
        mean_texture = request.form['mean_texture']
        mean_perimeter = request.form['mean_perimeter']
        mean_area = request.form['mean_area']
        mean_smoothness = request.form['mean_smoothness']
        mean_compactness = request.form['mean_compactness']
        mean_concavity = request.form['mean_concavity']
        mean_concave_points = request.form['mean_concave_points']
        mean_symmetry = request.form['mean_symmetry']
        mean_symetry = request.form['mean_symetry']
        mean_fractal_dimension = request.form['mean_fractal_dimension']
        radius_error = request.form['radius_error']
        texture_error = request.form['texture_error']
        perimeter_error = request.form['perimeter_error']
        area_error = request.form['area_error']
        smoothness_error = request.form['smoothness_error']
        compactness_error = request.form['compactness_error']
        concavity_error = request.form['concavity_error']
        concave_points_error = request.form['concave_points_error']
        symmetry_error = request.form['symmetry_error']
        fractal_dimension_error = request.form['fractal_dimension_error']
        worst_radius = request.form['worst_radius']
        worst_texture = request.form['worst_texture']
        worst_perimeter = request.form['worst_perimeter']
        worst_area = request.form['worst_area']
        worst_smoothness = request.form['worst_smoothness']
        worst_compactness = request.form['worst_compactness']
        worst_concave_points = request.form['worst_concave_points']
        worst_symmetry = request.form['worst_symmetry']
        worst_fractal_dimension = request.form['worst_fractal_dimension']

        mycursor.execute("insert into  report(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness,
                       mean_concavity, mean_concave_points, mean_symmetry, mean_symetry, mean_fractal_dimension,
                       radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error,
                       concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius,
                       worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concave_points,
                       worst_symmetry, worst_fractal_dimension))
        mydb.commit()
        mycursor.close()
        #return "sucess"
        input_list = [[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness,
                       mean_concavity, mean_concave_points, mean_symmetry, mean_symetry, mean_fractal_dimension,
                       radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error,
                       concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius,
                       worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concave_points,
                       worst_symmetry, worst_fractal_dimension]]
        ob = KNNeighbors()
        result1 = ob.make_prediction('KNeighborsClassifier', input_list)
        print(" Prediction is ", result1 )
        return " Prediction is " + result1[0]
    return render_template('main.html')







@app.route('/loginuser', methods=["GET", "POST"])
def loginuser():
    error = None
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        sql = "select * from userinfo where email='" + email + "' and password='" + password + "'"
        db = Data()
        c = db.getdata(sql)

        if c.rowcount > 0:
            c.close()
            # fetch quetions
            db.disconnect()
            session['username'] = email

            # return render_template("index.html")
            return redirect(url_for('main'))
        else:
            error = 'Invalid Username or Password. Please try again!'
            # return render_template("login.html")

    return render_template("main.html", error=error)


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/registeruser', methods=["GET", "POST"])
def registeruser():
    print(request.method)
    if request.method == 'POST':
        print("1")
        name = request.form['name']
        print("2")
        phone = request.form['phone']
        print("3")
        date = request.form['date']
        print("4")
        dept = request.form['dept']
        print("5")
        email = request.form['email']
        print("6")
        password = request.form['password']
        print("7")
        sql = "insert into userinfo(name,phone,date,dept,email,password) values('" + name + "','" + phone + "','" + date + "','" + dept + "','" + email + "','" + password + "')"
        db = Data()
        print("8")
        db.executeSQL(sql)
        print("9")
        db.disconnect()

        flash("Registered Successfully!")

        return redirect(request.url)

    return render_template("register.html")


@app.route('/main')
def main():
    return render_template("main.html")


@app.route('/about')
def about():
    return render_template("news-detail.html")


@app.route('/read')
def read():
    return render_template("read-more.html")


@app.route('/naive')
def naive():
    return render_template("naive-bayes.html")


@app.route('/logistic')
def logistic():
    return render_template("logistic-regression.html")


if __name__ == '__main__':
    app.run(debug=True)
