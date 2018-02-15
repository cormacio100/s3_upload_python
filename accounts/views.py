# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import env

from django.shortcuts import render, get_object_or_404, redirect
import base64
import hashlib
import hmac
import logging
import os
import time
#import urllib
import six.moves.urllib as urllib
#import urllib.parse
from urlparse import urlparse
from hashlib import sha1
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

##########################################
#   LOGGING
##########################################
import logging
logger = logging.getLogger(__name__)

# Create your views here.

def get_index(request):
    return render(request, 'accounts/index.html')


"""
View displays the upload form
"""
def upload(request):
    return render(request,'accounts/upload.html')

"""
View responsible for:
    -   generating and returning the signature with which the client-side Javascript can upload the image
The View:
    -   receives request for signature and S3 Bucket name is loaded from (HEROKU) environment
    -   File name and MIME type extracted from GET parameters
    -   S3 Client is constructed using boto3 library
        -   AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY set earlier are automatically read from the environment
    -   Pre-signed POST request is then generated using the generate_presigned_post function
Returned:
    -   The pre-signed request data and the location of the eventual file on S3 are returned to the client as JSON
"""
@csrf_exempt
def sign_s3(request):
    logger.debug('welcome to sign_s3')
    """
    https://devcenter.heroku.com/articles/s3-upload-python
    """
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET = os.environ.get('S3_BUCKET')

    logger.debug('AWS_ACCESS_KEY is '+AWS_ACCESS_KEY)
    logger.debug('AWS_SECRET_KEY is ' + AWS_SECRET_KEY)
    logger.debug('S3_BUCKET is ' + S3_BUCKET)

    #object_name = urllib.parse.quote_plus('1_AIC.jpg')
    #object_name = urllib.parse.quote_plus(request.POST.get('file_name'))
    #object_name = urllib.parse.quote_plus(request.POST['file_name'])
    object_name = urllib.parse.quote_plus(request.GET['file-name'])
    logger.debug('object_name is '+object_name)
    #object_name = urllib.parse.quote_plus(request.GET['file_name'])
    #object_name = urllib.pathname2url(request.GET['file_name'])
    #object_name = urlparse.quote_plus(request.GET['file_name'])
    #object_name = urllib.quote_plus(request.GET['file_name'])from urlparse import urlparse
    #mime_type = request.GET['file_type']
    mime_type = request.GET['file-type']

    secondsPerDay = 24*60*60
    expires = int(time.time()+secondsPerDay)
    amz_headers = "x-amz-acl:public-read"

    string_to_sign = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

    encodedSecretKey = AWS_SECRET_KEY.encode()
    encodedString = string_to_sign.encode()
    logger.debug('encoded string is '+encodedString)

    h = hmac.new(encodedSecretKey,encodedString,sha1)
    logger.debug('h is ')
    logger.debug(h)
    hDigest = h.digest()
    logger.debug('hDigest is ')
    logger.debug(hDigest)
    #signature = base64.encodebytes(hDigest).strip()
    signature = base64.encodestring(hDigest).strip()
    signature = urllib.parse.quote_plus(signature)
    #url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)
    url = 'https://s3.us-east-2.amazonaws.com/%s/%s' % (S3_BUCKET, object_name)
    #https: // s3.us - east - 2.amazonaws.com / file - upload - cormac - s3 / course_goals.txt

    signed_request = '%s?AWSAccessKeyId=%s&Expires=%s&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature)
    logger.debug('signed_request is ')
    logger.debug(signed_request)

    return JsonResponse({
        'signed_request': signed_request,
        'url': url,
    })

@csrf_exempt
def submit_form(request):
    """
    username = request.form['username']
    full_name = request.form['full_name']
    avatar_url = request.form['avatar_url']
    """
    username = 'username'
    full_name = 'full_name'
    avatar_url = 'avatar_url'
    update_account(username,full_name,avatar_url)
    #return redirect(url_for('accounts/profile'))
    return render(request, 'accounts/profile.html')


def update_account(username,full_name,avatar_url):
    print 'account updated'

"""
def profile(request):
    return render(request, 'accounts/upload.html')
"""