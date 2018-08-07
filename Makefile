.PHONY: build run

img=img/one.jpg
qual=85

build:
	docker build -t python3-ela .

run:
	docker run -it --rm -v "${PWD}/img":/ela/img python3-ela python ela.py $(img) $(qual)
