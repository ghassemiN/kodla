build:
	docker build --tag ghassemin/kodla:latest .

run:
	docker run -d -p 8080:5000 --name kodla ghassemin/kodla:latest

remove:
	docker rm -f kodla

logs:
	docker logs kodla

restart:
	$(MAKE) build 
	$(MAKE) remove
	$(MAKE) run