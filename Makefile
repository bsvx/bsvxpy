init:
	pip install -r requirements.txt
	pip install .

remake:
	pip uninstall bsvxpy
	pip install .

test:
	pytest