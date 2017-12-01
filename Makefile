all: install_tk install_requirements

install_tk:
	sudo apt-get install python3-tk

install_requirements:
	pip install -r requirements.txt