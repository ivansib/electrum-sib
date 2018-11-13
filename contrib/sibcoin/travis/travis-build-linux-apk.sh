#!/bin/bash
set -ev

if [[ -z $TRAVIS_TAG ]]; then
  echo TRAVIS_TAG unset, exiting
  exit 1
fi

BUILD_REPO_URL=https://github.com/akhavr/electrum-sibcoin.git

cd build

git clone --branch $TRAVIS_TAG $BUILD_REPO_URL electrum-sibcoin

docker run --rm \
    -v $(pwd):/opt \
    -w /opt/electrum-sibcoin \
    -t zebralucky/electrum-sibcoin-winebuild:Linux /opt/build_linux.sh

sudo find . -name '*.po' -delete
sudo find . -name '*.pot' -delete

sudo chown -R 1000 electrum-sibcoin

docker run --rm \
    -v $(pwd)/electrum-sibcoin:/home/buildozer/build \
    -t zebralucky/electrum-sibcoin-winebuild:KivyPy36 bash -c \
    'rm -rf packages && ./contrib/make_packages && ./contrib/make_apk'
