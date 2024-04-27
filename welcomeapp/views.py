from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    res=HttpResponse("""<html>
                     <body bgcolor=cyan>
                     <center>
                     <h1>welcome to home
                     </h1></center></body>
                     </html>""")
    return res