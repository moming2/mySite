# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import MySQLdb
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def main(request):
    return render_to_response('html/main.html')

@csrf_exempt
def count(request):
    # objDict = []
    conn = MySQLdb.connect('localhost', 'root', 'abc.123', 'django_chart', charset='utf8')
    cursor = conn.cursor()
    if request.method == "POST":
        name = request.POST.get('Line')
        if name == "canvasLine":
            sql = 'select name,sum(salary) as sum from app_chart group by name'
            cursor.execute(sql)
            result = cursor.fetchall()
            # for row in result:
            #     objDict.append(row)
    return HttpResponse(json.dumps(result))