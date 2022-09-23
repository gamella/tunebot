# tunebot

## How to build and run

Use Makefile command

$ make build
`docker build -t tunebot .``

$ make run
`docker run -p 8501:8501 tunebot`

```
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.
  You can now view your Streamlit app in your browser.
  URL: http://0.0.0.0:8501
```

See your browser http://localhost:8501/

$ make rm
`docker rm -f tunebot`
