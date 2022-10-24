# Description

A python application used to test integration with webhooks. 

# Getting Started

1. Create new virtual environment with `python -m venv ./venv`
2. Activate virtual environment with `source ./venv/bin/activate` or `/venv/Scripts/activate` otherwise.
3. Install packages. 
4. Run application with `python -m flook`
5. In a separate terminal, run `python test.py` to hit the /hook endpoint and simulate a webhook. Alternatively, use Postman and copy the data in test.py to make a POST request.