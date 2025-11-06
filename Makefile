.PHONY: run stop

start-dev:
	./start-dev.sh

start-prod:
	./start-prod.sh

reload:
	./start-reload.sh

stop:
	killall main.py
	
