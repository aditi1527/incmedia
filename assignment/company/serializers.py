
from rest_framework import serializers
from models import Company,FundingDetails, Market

class BaseCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class FundingSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='company.name')
    investor_company = BaseCompanySerializer(read_only=True)
    class Meta:
        model = FundingDetails
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    funding_details = FundingSerializer(many=True,source='company')
    markets = MarketSerializer(many=True,source='market')
    class Meta:
        model = Company
        fields = '__all__'

class FundingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingDetails
        fields = '__all__'

class CompanyPostSerializer(serializers.ModelSerializer):
    company = FundingSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

class CompanyPostSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
