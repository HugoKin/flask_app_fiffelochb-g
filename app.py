from flask import Flask, render_template, request, flash
 
app = Flask(__name__)
app.secret_key = "hugo2001"
 
 
@app.route("/hello")
def render():
   flash("Fyll i uppgifterna så svarar vi så snart vi kan.")
   return render_template("index.html")
 
 
@app.route("/output", methods=["POST", "GET"])
def output():
   flash("Hej " + str(request.form['name_input']) + "! Vi på Fiffel & Båg AB är glada att just du vill sälja din " + str(request.form['bilmärke_input']) + " av model " + str(request.form['bilmodel_input']) + " från " + str(request.form['orsmodel_input']) + ". Med tanke på att bilen bara gått " + str(request.form['mil_input']) + " mil är din bil av intresse för oss. Vi hoppas kunna få till en affär som gynnar båda parter.")
   return render_template("index.html")
 




