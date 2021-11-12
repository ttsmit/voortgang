# Voortgang
Klein python script om voortgang van twee groepen te laten zien. 

# Requirements
Besides python, the script requires `opencv-python`. Run to install:
```bash
pip install opencv-python
```

# Usage
Run `python process.py`. Values for the progress bars are read from the first line of two (included) files: *herten* and *zwijenen*. One can use any text editor to change these values. Alternatively, one can use a terminal command such as `echo "69" > herten` to quickly enter values into the files. 

The progress bars will be displayed full-screen.
