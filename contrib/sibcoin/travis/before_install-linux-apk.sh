#!/bin/bash
set -ev

if [[ -z $TRAVIS_TAG ]]; then
  echo TRAVIS_TAG unset, exiting
  exit 1
fi

docker pull zebralucky/electrum-sibcoin-winebuild:Linux
docker pull zebralucky/electrum-sibcoin-winebuild:KivyPy36
