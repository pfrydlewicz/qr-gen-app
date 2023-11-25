FROM python:3.10

# 
WORKDIR /build
# First copy dependencies definition only
COPY ./qr-gen-app/requirements.txt /build/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /build/requirements.txt

# now copy the rest. Do copy incrementally to facilitate docker cached builds.
COPY ./qr-gen-app /build/app

CMD ["uvicorn", "--app-dir", "app", "app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
