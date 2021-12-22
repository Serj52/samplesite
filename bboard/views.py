from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb
from . serializers import RubricSerializer


def index():
    pass