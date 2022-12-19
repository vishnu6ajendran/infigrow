from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken
import json
from django.core.cache import cache
import logging
logger = logging.getLogger(__name__)

# Example for catch function
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        cache.set('my_key', 'hello, world!', 30)
        content = {'message': cache.get('my_key')}
        return Response(content)

class SwapView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        path = "/home/vishnu/Pictures/inter2/infigrow/ledger recurrent match.json"
        contents = {}
        with open(path, 'r') as j:
            contents = json.loads(j.read())
        print(contents)
        ledger1 = request.data.get('ledger1')
        ledger2 = request.data.get('ledger2')
        data_ledger1 = contents.get(ledger1)
        data_ledger2 = contents.get(ledger2)
        swap_data_ledger1 = data_ledger1.get('recurrent_amount')
        swap_data_ledger2 = data_ledger2.get('recurrent_amount')
        data_ledger1['recurrent_amount'] = swap_data_ledger2
        data_ledger2['recurrent_amount'] = swap_data_ledger1
        data_ledger1_month = ''
        data_ledger2_month = ''
        for k,v in data_ledger1.get('data').items():
            if swap_data_ledger2 in v :
                data_ledger1_month = k
            data_ledger1['data'][k] = [swap_data_ledger2]
        for k,v in data_ledger2.get('data').items():
            if swap_data_ledger1 in v :
                data_ledger2_month = k
            data_ledger2['data'][k] = [swap_data_ledger1]
        final_data = {
            ledger1:data_ledger1,
            ledger2:data_ledger2,
            "month":"Ledger1 is month of "+data_ledger1_month+" and Ledger2 is month of "+data_ledger2_month+"."
        }
        print(final_data)
        return Response(final_data)

class MoveView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        path = "/home/vishnu/Pictures/inter2/infigrow/ledger recurrent match.json"
        contents = {}
        with open(path, 'r') as j:
            contents = json.loads(j.read())
        print(contents)
        ledger1 = request.data.get('ledger1')
        ledger2 = request.data.get('ledger2')
        data_ledger1 = contents.get(ledger1)
        data_ledger2 = contents.get(ledger2)
        swap_data_ledger1 = data_ledger1.get('recurrent_amount')
        swap_data_ledger2 = data_ledger2.get('recurrent_amount')
        data_ledger1['recurrent_amount'] = 0
        data_ledger2['recurrent_amount'] = swap_data_ledger1
        data_ledger1_month = ''
        data_ledger2_month = ''
        for k, v in data_ledger1.get('data').items():
            if swap_data_ledger2 in v:
                data_ledger1_month = k
            data_ledger1['data'][k] = [0]
        for k, v in data_ledger2.get('data').items():
            if swap_data_ledger1 in v:
                data_ledger2_month = k
            data_ledger2['data'][k] = [swap_data_ledger1]
        final_data = {
            ledger1: data_ledger1,
            ledger2: data_ledger2,
            "month": "Ledger1 is month of " + data_ledger1_month + " and Ledger2 is month of " + data_ledger2_month + "."
        }
        print(final_data)
        return Response(final_data)
class User(APIView):
    def post(self,request):
        error = False
        if request.user.is_authenticated:
            return redirect('home')
        if request.method == "POST":
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                token = RefreshToken.for_user(user)
                token_data = {"refresh":str(token),"access":str(token.access_token)}
                response = {'success': 'true', 'token': token_data, 'user': user.id}
                logger.info('user authentication success')
                return Response(response)
            else:
                response = {'success': 'false', 'token': {}}
                logger.warning('user authentication fail')
                return Response(response)