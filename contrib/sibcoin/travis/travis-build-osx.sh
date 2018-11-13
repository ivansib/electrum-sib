#!/bin/bash
set -ev

if [[ -z $TRAVIS_TAG ]]; then
  echo TRAVIS_TAG unset, exiting
  exit 1
fi

BUILD_REPO_URL=https://github.com/akhavr/electrum-sibcoin.git

cd build

git clone --branch $TRAVIS_TAG $BUILD_REPO_URL electrum-sibcoin

cd electrum-sibcoin

export PY36BINDIR=/Library/Frameworks/Python.framework/Versions/3.6/bin/
export PATH=$PATH:$PY36BINDIR
source ./contrib/sibcoin/travis/electrum_sibcoin_version_env.sh;
echo wine build version is $SIBCOIN_ELECTRUM_VERSION

sudo pip3 install --upgrade pip
sudo pip3 install -r contrib/deterministic-build/requirements.txt
sudo pip3 install \
    x11_hash>=1.4 \
    pycryptodomex==3.6.1 \
    btchip-python==0.1.27 \
    keepkey==4.0.2 \
    safet==0.1.3 \
    trezor==0.10.2

pyrcc5 icons.qrc -o electrum_sibcoin/gui/qt/icons_rc.py

export PATH="/usr/local/opt/gettext/bin:$PATH"
./contrib/make_locale
find . -name '*.po' -delete
find . -name '*.pot' -delete

cp contrib/sibcoin/osx.spec .
cp contrib/sibcoin/pyi_runtimehook.py .
cp contrib/sibcoin/pyi_tctl_runtimehook.py .

pyinstaller \
    -y \
    --name electrum-sibcoin-$SIBCOIN_ELECTRUM_VERSION.bin \
    osx.spec

info "Adding Sibcoin URI types to Info.plist"
plutil -insert 'CFBundleURLTypes' \
   -xml '<array><dict> <key>CFBundleURLName</key> <string>sibcoin</string> <key>CFBundleURLSchemes</key> <array><string>sibcoin</string></array> </dict></array>' \
   -- dist/Sibcoin-Electrum.app/Contents/Info.plist \
   || fail "Could not add keys to Info.plist. Make sure the program 'plutil' exists and is installed."

sudo hdiutil create -fs HFS+ -volname "Sibcoin-Electrum" \
    -srcfolder dist/Sibcoin-Electrum.app \
    dist/Sibcoin-Electrum-$SIBCOIN_ELECTRUM_VERSION-macosx.dmg
