try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'URL to get it'
	'download_url': 'where to get it',
	'author_email': 'xushen1122@sina.com',
	'version': '0.1',
	'install_requires':['nose'],
	'packages': ['NAME'],
	'scripts':[],
	'name':'projectname'

	}

	setup(**config)