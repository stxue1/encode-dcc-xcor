FROM quay.io/encode-dcc/xcor:latest

ENV PYTHONPATH /home/encode/
# python multiproccessing.cpu_count() is not accurate under slurm
# https://stackoverflow.com/a/50029433
# https://github.com/moby/moby/issues/29110#issuecomment-274339807
USER root
COPY envwrapper /home/encode/
RUN mv /home/encode/envwrapper /bin/envwrapper
RUN chmod 755 /bin/envwrapper
COPY sitecustomize.py /home/encode/sitecustomize.py
USER encode
ENTRYPOINT ["envwrapper", "python", "/image_software/pipeline-container/src/xcor.py"]