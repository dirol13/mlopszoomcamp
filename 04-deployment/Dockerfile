FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

RUN pip install -U pip & pip install pipenv

COPY model2.bin model.bin
COPY homework.py homework.py
COPY [ "Pipfile", "Pipfile.lock", "./" ]
RUN pipenv install --system --deploy

ENTRYPOINT ["python", "homework.py"]