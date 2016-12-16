# PyQt5, Python3 and Custom C++ Widgets

This boilerplate repository shows how to combine PyQt5 and custom Qt widgets written in C++.


## Prerequisits

Obviuously, you need working installations of Python3, Qt5 and PyQt5.

Python bindings for custom C++ library are created with SIP. So you need to install SIP packages:

```sh
sudo apt-get install pyqt5-dev python3-pyqt5 python3-sip python3-sip-dev sip-dev
```


## Build the example library

```sh
cd custom
qmake
make
```


## Build the python extension & run test
```sh
cd python
./build.sh
```
