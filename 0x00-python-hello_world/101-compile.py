#!/bin/bash
python3 -c "import py_compile; py_compile.compile('$PYFILE', '`echo $PYFILE`c')"