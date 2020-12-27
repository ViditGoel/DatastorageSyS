from flask import Flask, render_template, redirect, url_for, request
from DATASTORAGE_SYS.CRD import DataStoreCRD

app=Flask(__name__)

@app.route('/CRD/create',methods=["GET","POST"])
def create():
    if request.method=="POST":
        KEY = request.form["KEY"]
        DATA1 = request.form["nm1"]
        DATA2 = request.form["nm2"]
        time_to_live = request.form["nm3"]
        obj = DataStoreCRD()
        READ, status_d = obj.create_data(KEY,DATA1,DATA2,time_to_live)
        return redirect(url_for("status",status=status_d))
    else:
        return render_template("KEY_VALUE.html")

@app.route('/CRD/read',methods=["GET","POST"])
def read():
    if request.method=="POST":
        KEY = request.form["KEY"]
        obj = DataStoreCRD()
        READ = obj.read_data(KEY)
        return redirect(url_for("read_values",read_values=READ))
    else:
        return render_template("READ.html")

@app.route('/CRD/delete',methods=["GET","POST"])
def delete():
    if request.method == "POST":
        KEY = request.form["KEY"]
        obj = DataStoreCRD()
        DELETE = obj.delete_data(KEY)
        return redirect(url_for("delete_values",delete_values=DELETE))
    else:
        return render_template("DELETE.html")

@app.route('/CRD/<delete_values>')
def delete_values(delete_values):
    return f"<h2>{delete_values}</h2>"

@app.route('/CRD/<read_values>')
def read_values(read_values):
    return f"<h2>{read_values}</h2>"

@app.route('/CRD/<status>')
def status(status):
    return f"<h1>{status}</h1>"

if __name__ == "__main__":
    app.run(debug=True)

