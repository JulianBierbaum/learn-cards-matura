#!/usr/bin/env bash

set -e
set -x

mypy ../app --ignore-missing-imports

