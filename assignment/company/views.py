# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from models import Company,FundingDetails
from serializers import *
from rest_framework.response import Response

# Create your views here.

class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    query_param_key = 'profile_id'
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'

class CompanyDetailPost(APIView):
    def post(self, request, format=None):
        response_data = {'success': False}
        data = request.data
        data['logo'] = request.FILES.get('logo')
        com = CompanyPostSerializer(data=data)
        if com.is_valid():
            com.save()
            response_data = {
                'success':True,
            }
        return Response(response_data)

class FundingDetailPost(APIView):
    serializer_class = FundingPostSerializer
    def post(self, request, format=None):
        response_data = {'success': False}
        data = request.data
        com = FundingPostSerializer(data=data)
        if com.is_valid():
            com.save()
            response_data = {
                'success':True,
            }
        return Response(response_data)

class CompanyDetailPost2(APIView):
    serializer_class = CompanyPostSerializer2
    def post(self, request, format=None):
        response_data = {'success': False}
        data = request.data
        data['logo'] = request.FILES.get('logo')
        com = CompanyPostSerializer2(data=data)
        if com.is_valid():
            com.save()
            response_data = {
                'success':True,
            }
        return Response(response_data)

