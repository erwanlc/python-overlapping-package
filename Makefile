clean:
	# @pyclean .
	@rm -fr dist
	@rm -fr build 
	@rm -fr proj-*.dist-info
	@rm -fr proj.egg-info

psi:
	@python setup.py install

test:
	@python setup.py test 

