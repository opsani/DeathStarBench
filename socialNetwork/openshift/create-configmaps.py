#!/usr/bin/env python

import os

CONFIG_MAPS = {
    "jaeger-config-yaml": "config/jaeger-config.yml",
    "nginx-thrift-jaeger": "../nginx-web-server/jaeger-config.json",
    "nginx-thrift-genlua": "../gen-lua",
    "nginx-thrift-pages": "../nginx-web-server/pages",
    "nginx-thrift-pages-style": "../nginx-web-server/pages/style",
    "nginx-thrift-pages-javascript": "../nginx-web-server/pages/javascript",
    "nginx-thrift-luascripts": "nginx-thrift-config/lua-scripts",
    "nginx-thrift-luascripts-api-home-timeline": "nginx-thrift-config/lua-scripts/api/home-timeline",
    "nginx-thrift-luascripts-api-post": "nginx-thrift-config/lua-scripts/api/post",
    "nginx-thrift-luascripts-api-user": "nginx-thrift-config/lua-scripts/api/user",
    "nginx-thrift-luascripts-api-user-timeline": "nginx-thrift-config/lua-scripts/api/user-timeline",
    "nginx-thrift-luascripts-wrk2-api-home-timeline": "nginx-thrift-config/lua-scripts/wrk2-api/home-timeline",
    "nginx-thrift-luascripts-wrk2-api-post": "nginx-thrift-config/lua-scripts/wrk2-api/post",
    "nginx-thrift-luascripts-wrk2-api-user": "nginx-thrift-config/lua-scripts/wrk2-api/user",
    "nginx-thrift-luascripts-wrk2-api-user-timeline": "nginx-thrift-config/lua-scripts/wrk2-api/user-timeline",
    "nginx-thrift": "../nginx-web-server/conf/nginx.conf",
    "media-frontend-nginx": "../media-frontend/conf/nginx.conf",
    "media-frontend-lua": "media-frontend-config/lua-scripts",
}

def create_config_maps(config_maps):
  os.system('kubectl create namespace social-network')
  for name, file in config_maps.items():
    os.system('kubectl create configmap {} --from-file={} --namespace social-network'.format(name,file))

if __name__ == '__main__':
  create_config_maps(CONFIG_MAPS)
