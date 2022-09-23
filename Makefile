build:
	docker build -t tunebot .

run:
	docker run -p 8501:8501 tunebot

rm:
	docker rm tunebot
