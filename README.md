# PY_call_MATLAB
***A simple tutorial which teaches you how to call MATLAB in python.***

* Step 1 - Clone this repository to local. Then, unzip and open the folder.
* Step 2 - Running `find_your_matlab.m` and you will get path. For examle, `C:\Program Files\MATLAB\R2020b\extern\engines\python`.
* Step 3 - Open your cmd (Anaconda Prompt is also acceptable), notice: please "execute as system administrator".
* Step 4 - Execute the command `cd C:\Program Files\MATLAB\R2020b\extern\engines\python` in your cmd, notice: here you should change path to what you get from last step.
* Step 5 - Execute the command `python setup.py install` in your cmd, then the coonection of Python and MATLAB is done.
* Step 6 - Execute the command `cd ...\py_call_matlab\` in your cmd, then `python main.py`.
* If cmd shows "Hello World.", it means your setup is successfully.

***Notice 1: this code only works when your python and MATLAB can independently***

***Notice 2: If you do not open cmd as an administrator, there may be a permission error ***
