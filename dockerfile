FROM python:3.11-slim

WORKDIR /app_dock_files
# copy the direct files
COPY images/data_should_like.PNG pipeline_model.pkl salesP_app.py requirements.txt tempCodeRunnerFile.py /app_dock_files/
# copy the files that inside the another folder
#COPY images/data_should_like.PNG /app_dock_files/

RUN pip install -r requirements.txt
EXPOSE 8502
#HEALTHCHECK cmd curl --fail http://localhost:8501/_stcore/health
HEALTHCHECK --interval=30s --timeout=10s CMD curl --fail http://localhost:8502/_stcore/health || exit 1

ENTRYPOINT [ "streamlit","run","salesP_app.py","--server.port=8502","--server.address=0.0.0.0"]