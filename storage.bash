#!/bin/bash

while true; do
    du -b -d 1 "weaviate-data" | awk '{ print "node_directory_size_bytes{directory=\"" $2 "\"} "  $1 }' > node-exporter-data/directory_size.prom
    sleep 5;
done
