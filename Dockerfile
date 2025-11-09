FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --no-build-isolation -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONMALLOC=malloc
ENV OPENBLAS_NUM_THREADS=1
ENV OMP_NUM_THREADS=1



COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
