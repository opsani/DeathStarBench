FROM bburdick/thrift-microservice-deps:xenial

#ARG NUM_CPUS=2

COPY ./ /social-network-microservices
RUN cd /social-network-microservices \
    && mkdir -p build \
    && cd build \
    && cmake .. \
    && make \
    && make install

WORKDIR /social-network-microservices
