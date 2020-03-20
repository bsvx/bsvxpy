init:
	pip install -r requirements.txt

remake:
	pip uninstall bsvxpy
	pip install .

test:
	pytest