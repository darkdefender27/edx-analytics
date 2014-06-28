from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext


def main(request):
    context = RequestContext(request)
    return render_to_response('base.html', context)


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def stats_one(request):
    context = RequestContext(request)
    return render_to_response('stats_one.html', context)


def stats_two(request):
    context = RequestContext(request)
    return render_to_response('stats_two.html', context)


def stats_three(request):
    context = RequestContext(request)
    return render_to_response('stats_three.html', context)


def stats_four(request):
    context = RequestContext(request)
    return render_to_response('stats_four.html', context)
