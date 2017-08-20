# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

STAGES_LIST = (('Series A', 'Series A'),
                ('Series B', 'Series B'),
                ('Series C', 'Series C'),
                ('Series D', 'Series D'),
                ('Series E', 'Series E'),
                ('Series F', 'Series F'),
                )

class Market(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class SocialFields(models.Model):
    '''
    This is an abstract model. It contains social fields
    '''
    contact_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    linkedInId = models.CharField(max_length=250,blank=True, null=True)
    twitter_link = models.URLField(max_length=300, blank=True)

    class Meta:
        app_label = 'company'
        abstract = True

class Company(SocialFields):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    website = models.URLField(max_length=300, blank=True)
    show_on_site = models.BooleanField(default=True)
    founded_on_date = models.DateTimeField(auto_now=True)
    market = models.ManyToManyField(Market,blank=True,null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        app_label = 'company'

class FundingDetails(models.Model):
    '''
    This is a 1:m (one to many) model that contains fields required for fundings
    '''
    funding_date = models.DateTimeField(null=True, blank=True)
    funding_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    stages  = models.CharField(max_length=50, choices=STAGES_LIST, blank=True, null=True)
    investor_company = models.ForeignKey(Company, null=True, related_name='investor_company')
    company = models.ForeignKey(Company, null=True,related_name='company')

    class Meta:
        app_label = 'company'
    def __unicode__(self):
        return unicode('%s:%s' % (self.company,self.investor_company))

