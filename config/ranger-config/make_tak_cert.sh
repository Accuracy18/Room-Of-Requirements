docker exec -it tak-server-tak-1 bash -c 'cd /opt/tak/certs/; ./makeCert.sh client "$@" ' -- $@
