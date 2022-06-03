@echo off

python -m pip install --upgrade pip
pip3 install -r requirements-dev.txt

echo .
echo echo -------- Finish Installing --------
echo .

timeout 100 > NUL