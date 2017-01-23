#-*- coding: utf-8 -*-
from flask import jsonify, request

from . import api


@api.app_errorhandler(404)
def page_not_found(e):
	'''
	Hata: aranılan sonuç bulunmadıysa
	'''
	if not request.accept_mimetypes.accept_json:
		return 'Json veri tipi kabul edilmiyor'
	response = jsonify({'status': 404, 'hata': 'aranilan bulunamadi'})
	response.status_code = 404
	return response
