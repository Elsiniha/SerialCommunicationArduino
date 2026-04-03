# SerialComunicationArduino
The goal of this project is to establish a method to link the pins of an Arduino to any python script running on the computer through a serial communication protocol.

## Installation Guide:

1. Clone the repository:
```
git clone https://github.com/Elsiniha/SerialCommunicationArduino.git
```

2. Using conda, the virtual environment can be created with:
```
conda env create -f environment.yml
```

3. To activate the environment, use:
```
conda activate ./SerialComPyEnv
```

## Contributing:

Once you are done so far and want to push some new code, update the environment.yml file first with:
```
conda env create --from-history > environment.yml
```

Ensure that the documentation stays up to date and follow Google's Python Style Guide for implemented code.