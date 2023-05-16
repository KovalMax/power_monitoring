FROM python:3.11
ENV PYTHONUNBUFFERED 1

WORKDIR /root
COPY . /root/

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN echo 'export PATH=$PATH' | tee -a /root/.bashrc

RUN pip install -U pip wheel setuptools
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8073"]