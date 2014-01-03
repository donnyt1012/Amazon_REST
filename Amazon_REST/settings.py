#-*- coding:utf-8 -*-

import os

SERVER_NAME = '127.0.0.1:5000'

MONGO_HOST = '*'
MONGO_PORT = 27017
MONGO_USERNAME = '*'
MONGO_PASSWORD = '*'
MONGO_DBNAME = '*'

RESOURCE_METHODS = ['GET']

ITEM_METHODS = ['GET']

commodity = {
	'item_title':'commodity',

	'additional_lookup': {
		'url': 'regex("[\w|\d]+")',
		'field': 'ASIN'
	},

	'schema': {
		'ASIN':{
			'type': 'String',
			'required': True,
			'unique': True,
		},
		'productInfo': {
			'type': 'list',
		},
		'offer': {
			'type': 'list',
		},
		'review': {
			'type': 'list',
		},
	},
}

DOMAIN = {
	'commodity':commodity,
}

ETAG = None
LINK = None