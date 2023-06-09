from flask import Flask, request
import json, dbherlper

app = Flask(__name__)

@app.post("/api/client")
def client_post():
    error = dbherlper.check_endpoint_info(request.json, ["username" , "password" , "is_premium"])
    if(error != None):
        return error
    
    results = dbherlper.run_procedure("call create_client(?,?,?)", [request.json.get("username"), request.json.get("password") , request.json.get("is_premium")])
    if(type(results) == list):
        return json.dump(results, default=str)
    else:
        return "sorry, something went wrong"
    
app.patch("/api/client")
def client_patch():
    error = dbherlper.check_endpoint_info(request.json, ["username" , "password" , "new_password"])
    if(error != None):
        return error
    results = dbherlper.run_procedure("call update_client(?,?,?)" , [request.json.get("username"), request.json.get("password") , request.json.get("new_password")])
    if(type(results) == list):
        return json.dump(results, default=str)
    else:
        return "sorry, something went wrong"
app.run (debug=True)