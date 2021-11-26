

# Create your views here.
from datetime import datetime
from .models import *
from django.shortcuts import render
from django.http import HttpRequest
import psycopg2
def index(request):
    return render(request, 'index.html')
def insert(request):
    return render(request, 'insert.html')
def error(request):
    return render(request, 'error.html')
def query(request):
    message = None
    if request.method == 'POST':
        if 'q1' == str(request.POST.get('query')):
            cust_id = request.POST.get('cust_id')
            list1 = [str(cust_id)]
            connection = psycopg2.connect(host="localhost", database="201901453_db", user="postgres", password="admin")
            cursor = connection.cursor()
            cursor.execute('SELECT version()')
            q1 = "select * from flight_tracking.customer1 where cust_id = %s"
            cursor.execute(q1, list1)
            message = "q1"
            rows = cursor.fetchall()
            connection.close()
        if 'q2'== str(request.POST.get('query')):
            pilot_id = request.POST.get('pilot_id')
            list1 = [str(pilot_id)]
            connection = psycopg2.connect(host="localhost", database="201901453_db", user="postgres", password="admin")
            cursor = connection.cursor()
            cursor.execute('SELECT version()')
            q1 = "select * from flight_tracking.pilot where pilot_id = %s"
            cursor.execute(q1, list1)
            message = "q2"
            rows = cursor.fetchall()
            connection.close()
        if 'q3'== str(request.POST.get('query')):
            plane_id = request.POST.get('plane_id')
            list1 = [str(plane_id)]
            connection = psycopg2.connect(host="localhost", database="201901453_db", user="postgres", password="admin")
            cursor = connection.cursor()
            cursor.execute('SELECT version()')
            q1 = "select plane_id, airline, date, time, schedule_status from flight_tracking.flight_scheduling where plane_id = %s"
            cursor.execute(q1, list1)
            message = "q3"
            rows = cursor.fetchall()
            connection.close()
        context = {'message': message, 'rows':rows}
        return render(request, 'query.html', context)
    else:
        return render(request, 'query.html', {'message': message})

    
def insert_flight1(request):
    if request.method == 'POST':
        connection = psycopg2.connect(host="localhost", database="201901453_db", user="postgres", password="admin")
        cursor = connection.cursor()
        cursor.execute('SELECT version()')
        list1 = [str(request.POST.get('id')), str(request.POST.get('airline'))]
        q1 = "insert into flight_tracking.flight1 values(%s, %s)"
        try:
            cursor.execute(q1, list1)
        except:
            return render(request, 'error.html') 
        connection.commit()
        connection.close()
        return render(request, 'insert_flight1.html')
    else :
        return render(request, 'insert_flight1.html')
def insert_customer1(request):
    if request.method == 'POST':
        connection = psycopg2.connect(host="localhost", database="201901453_db", user="postgres", password="admin")
        cursor = connection.cursor()
        cursor.execute('SELECT version()')
        cust_id = request.POST.get('cust_id')
        ticket_id = request.POST.get('ticket_id')
        name = request.POST.get('name')
        date = request.POST.get('date')
        plane_id = request.POST.get('plane_id')
        list1 = [str(cust_id), str(ticket_id), str(name), str(date), str(plane_id)]
        q1 = "insert into flight_tracking.customer1 values(%s, %s, %s, %s, %s)"
        try:
            cursor.execute(q1, list1)
        except:
            return render(request, 'error.html') 
        connection.commit()
        connection.close()
        return render(request, 'insert_customer1.html')
    else :
        return render(request, 'insert_customer1.html')
