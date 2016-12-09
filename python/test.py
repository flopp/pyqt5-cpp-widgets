#!/usr/bin/env python3

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Custom

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # create the Custon Widget
    w = Custom.Widget()
    w.setText("This is the Custom.Widget!")
    w.show()
    
    rc = app.exec_()
    
    # explicit deletion of w & app to avoid segfault on exit
    del w
    del app
    
    sys.exit(rc)
