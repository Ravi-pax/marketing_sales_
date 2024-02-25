FROM python:3.11-slim

WORKDIR /app_dock_files
# copy the direct files
COPY pipeline_model.pkl salesP_app.py requirements.txt tempCodeRunnerFile.py /app_dock_files/
# copy the files that inside the another folder
COPY images/ /app_dock_files/images/

RUN pip install -r requirements.txt
EXPOSE 8501
HEALTHCHECK cmd curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT [ "streamlit","run","salesP_app.py","--server.port=8501","--server.address=0.0.0.0"]