#!/bin/sh

mkdir target
(cd src/api; zip -r ../../target/api.zip .)
(cd src; zip -r ../target/infrastructure.zip python/infrastructure)
(cd src; zip -r ../target/psycopg2.zip python/psycopg2)