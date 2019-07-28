from flask import *
from flask_compress import Compress
import os
import pickle

compress = Compress()
app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/')
def main():
   return render_template("main.html")

#debug

@app.route('/dbg')
def dbg_main_root():
   return render_template("debug.html")

@app.route('/dbg/index.html')
def dbg_main_root_s():
   return render_template("debug.html")


@app.route('/dbg/index.html')
def dbg_main():
   return render_template("debug.html")

@app.route('/dbg/exit/true')
def dbg_setexit_true():
   check = '1'
   with open('ck/data1.ck', 'wb') as file:
      pickle.dump(check, file)
      return "changed", check

@app.route('/dbg/exit/false')
def dbg_setexit_false():
   check = '0'
   with open('ck/data1.ck', 'wb') as file:
      pickle.dump(check, file)
      return "changed", check

@app.route('/dbg/person/false')
def dbg_setperson_false():
   check = '0'
   with open('ck/data2.ck', 'wb') as file:
      pickle.dump(check, file)
      return "changed", check

@app.route('/dbg/person/true')
def dbg_setperson_true():
   check = '0'
   with open('ck/data2.ck', 'wb') as file:
      pickle.dump(check, file)
      return "changed", check

@app.route('/dbg/status/false')
def dbg_setstatus_false():
   check = '0'
   with open('ck/data3.ck', 'wb') as file:
      pickle.dump(check, file)
      return "changed",check

@app.route('/dbg/status/true')
def dbg_setstatus_true():
   check = '1'
   with open('ck/data3.ck', 'wb') as file:
      pickle.dump(check, file)
      return "changed",check


@app.route('/dbg/exit/look')
def dbg_checkexit():
   with open('ck/data1.ck', 'rb') as file:
      check = pickle.load(file)
      print(check)
      return check

@app.route('/dbg/status/look')
def dbg_checkstatus():
   with open('ck/data3.ck', 'rb') as file:
      check = pickle.load(file)
      print(check)
      return check


@app.route('/dbg/person/look')
def dbg_checkperson():
   with open('ck/data2.ck', 'rb') as file:
      check = pickle.load(file)
      print(check)
      return check


#debug end

@app.route('/runexit')
def setexit_true():
   check = '1'
   with open('ck/data1.ck', 'wb') as file:
      pickle.dump(check, file)
      return check
 

@app.route('/checkexit')
def checkexit():
   with open('ck/data2.ck', 'rb') as file:
      check = pickle.load(file)
      print(check)
      return check

@app.route('/checkstatus')
def checkstatus():
   with open('ck/data3.ck', 'rb') as file:
      check = pickle.load(file)
      print(check)
      return check


@app.route('/checkperson')
def checkperson():
   with open('ck/data2.ck', 'rb') as file:
      check = pickle.load(file)
      print(check)
      return check

if __name__ == '__main__':
   app.debug = True
   check = '0'
   with open('ck/data2.ck', 'wb') as file:
      pickle.dump(check, file)
   with open('ck/data3.ck', 'wb') as file:
      pickle.dump(check, file)
   with open('ck/data1.ck', 'wb') as file:
      pickle.dump(check, file)
   app.run(host="0.0.0.0", threaded=True, port=80)

