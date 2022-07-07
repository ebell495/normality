FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /normality
WORKDIR /normality
RUN python3 -m pip install . && chmod +x fuzz/normalization-fuzz.py
