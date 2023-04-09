FROM python:3.10 as build

RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH

ADD ./ /code
WORKDIR /code
RUN /venv/bin/python -m pip install -r /code/requirements.txt
RUN /venv/bin/python -m pip install /code

FROM python:3.10-slim as runtime
COPY --from=build /venv/ /venv/
ENV PATH=/venv/bin:$PATH

ENTRYPOINT ["pycraft-chat-server"]
CMD ["-H","minecraft"]

