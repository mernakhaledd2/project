name: Python CI/CD

on:
  push:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python 3.x
        uses: actions/setup-python@v3
        with:
          python-version: '3.x'  

      - name: Run Python script
        run: python ./hello.py  
