from pyscript import *
from js import document, window

def greet(event):
    document.getElementById("greeting").innerHTML = "Hello, " + document.getElementById("name").value + "!"