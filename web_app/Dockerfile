FROM python:3.8-slim
WORKDIR /app
ADD . /app
RUN python -m pip install --upgrade pip
RUN pip install flask
RUN pip install numpy
RUN pip install scikit-learn
RUN pip install pandas
RUN pip install torch
RUN pip install scikit-learn joblib
EXPOSE 5000
ENV NAME Opentoall
CMD ["python","app.py"]


