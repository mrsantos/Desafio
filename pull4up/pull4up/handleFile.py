# -*- coding: utf-8 -*-

from models import Desafio

def handle_uploaded_file(f):

	l = [i.strip('\n') for i in f.readlines()[1:]]
	
	for i in l:
		(nome, desc, preco, ncompras, ende, comer) = i.split("\t")
		data = Desafio(purchaser_name=nome, item_description=desc, item_price=preco, purchase_count=ncompras, merchant_address=ende,merchant_name=comer)
		data.save()
		print nome
