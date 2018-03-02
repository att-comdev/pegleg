#!/usr/bin/env bash

set -e

realpath() {
    [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}

SCRIPT_DIR=$(realpath "$(dirname "${0}")")
SOURCE_DIR=${SCRIPT_DIR}/pegleg
if [ -d "$PWD/global" ]; then
  WORKSPACE="$PWD"
else
  WORKSPACE=$(realpath "${SCRIPT_DIR}/..")
fi

IMAGE_PEGLEG=${IMAGE_PEGLEG:-quay.io/attcomdev/pegleg:latest}

if [[ -z ${http_proxy} && -z ${https_proxy} ]]
then
    docker build --network=host -q --rm -t "${IMAGE_PEGLEG}" "${SOURCE_DIR}" > /dev/null
else
    docker build --network=host -q --rm -t "${IMAGE_PEGLEG}" --build-arg http_proxy=${http_proxy} --build-arg https_proxy=${https_proxy}  "${SOURCE_DIR}" > /dev/null
fi

docker run --net=host --rm -t \
    -v "${WORKSPACE}:/var/pegleg" \
    "${IMAGE_PEGLEG}" \
    pegleg "${@}"
