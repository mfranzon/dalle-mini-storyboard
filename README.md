# DALL-E StoryBoard

A Streamlit app based on the [DALL-E Playground](https://github.com/saharmor/dalle-playground), with the frontent part also in Python.

Load a story and create images for each chapter. A simple summarization method is implemented in [summary.py](summary.py). If a chapter is greater than 15 words it will be summarize using `"sshleifer/distilbart-cnn-12-6"`.

Create your storyboard from text using DALL-E!

## Requirements

```console
$ pip install jupyterlab requests streamlit 
```

## Backend:
Go to [DALL-E Playground](https://github.com/saharmor/dalle-playground), run the Google Colab or if you have enough memory or a GPU available you can also run it locally. 

To have it locally: 
- clone the above repo
- install the requirements
- run this code into a Jupyter cell

```python
from threading import Thread

dalle_model = 'Mini'
app_port = 8000

def app():
  print(f"Selected DALL-E Model - [{dalle_model}]")
  !python dalle-playground/backend/app.py --port {app_port} --model_version {dalle_model} --save_to_disk true --img_format jpeg --output_dir generations

if __name__ == '__main__':
    t1 = Thread(target = app)
    a = t1.start()
```
Then copy the backend url into [dalle.py](dalle.py).

## Frontend

To run the streamlit application: 

```console
$ streamlit run main.py
```

## Input file

The input file is a .txt in which each chapter you want to rappresent as image is separated from the other with `!!!` like the example [file](test.txt)