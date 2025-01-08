FROM python:3-alpine

WORKDIR D:\vscode\echobots_flet\echobots\src\main.py

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]