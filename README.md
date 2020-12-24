# humen-face-emotions and action -analysis
humen face emotions and actions analysis using dlib and opencv 


## How the code works??
The python code detects different landmarks on the face and predicts the emotions and action such as smile , talking action , eye acts , based on it. It automatically takes a photo of that person when he smiles. 
## How to install the project and various other modules??
The project was done long back so it would be working properly only if you install particular versions of each module.
#Python Version used for project - 2.7.13 (32 bit version)
1. CMAKE - 0.6.0 (install using pip)
2. DLIB - 18.17.100(install using pip)
3. NUMPY - https://sourceforge.net/projects/numpy/files/NumPy/1.10.0/numpy-1.10.0-win32-superpack-python2.7.exe/download (Download the file and install using pip)
4. OPENCV - https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv (Download the first file - opencv_python‑2.4.13.5‑cp27‑cp27m‑win32.whl and install using pip)
5. PYGAME - 1.9.3 (install using pip)

### Detecting Different facial expressions:
To detect smile in a face, points 49 and 50 are considered. 

to detect talking action on face , point 68 and 68 are considered.

To detect left eye brow movement(lifting up), points 38 and 41 are considered. 

Similarly to detect right eye brow movement(lifting up), points 44 and 47 are considered. 
