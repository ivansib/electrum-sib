# -*- mode: python -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules, collect_dynamic_libs

import sys
for i, x in enumerate(sys.argv):
    if x == '--name':
        cmdline_name = sys.argv[i+1]
        break
else:
    raise Exception('no name')

PYHOME = 'c:/python3'

home = 'C:\\electrum-sib\\'

# see https://github.com/pyinstaller/pyinstaller/issues/2005
hiddenimports = []
hiddenimports += collect_submodules('trezorlib')
hiddenimports += collect_submodules('safetlib')
hiddenimports += collect_submodules('btchip')
hiddenimports += collect_submodules('keepkeylib')
hiddenimports += collect_submodules('websocket')
hiddenimports += collect_submodules('ckcc')

# safetlib imports PyQt5.Qt.  We use a local updated copy of pinmatrix.py until they
# release a new version that includes https://github.com/archos-safe-t/python-safet/commit/b1eab3dba4c04fdfc1fcf17b66662c28c5f2380e
hiddenimports.remove('safetlib.qt.pinmatrix')


# Add libusb binary
binaries = [(PYHOME+"/libusb-1.0.dll", ".")]


# Add libx11hash binary
binaries += [(PYHOME+"/libx11hash-0.dll", ".")]

# Add libx11_gost_hash binary
binaries += [(PYHOME+"/x11_gost_hash/libx11_gost_hash-0.dll", "x11_gost_hash")]

# Workaround for "Retro Look":
binaries += [b for b in collect_dynamic_libs('PyQt5') if 'qwindowsvista' in b[0]]

binaries += [('C:/tmp/libsecp256k1.dll', '.')]

datas = [
    (home+'electrum_sibcoin/*.json', 'electrum_sibcoin'),
    (home+'electrum_sibcoin/wordlist/english.txt', 'electrum_sibcoin/wordlist'),
    (home+'electrum_sibcoin/locale', 'electrum_sibcoin/locale'),
    (home+'electrum_sibcoin/plugins', 'electrum_sibcoin/plugins'),
    ('C:\\Program Files (x86)\\ZBar\\bin\\', '.'),
    (home+'icons', 'icons'),
]
datas += collect_data_files('trezorlib')
datas += collect_data_files('safetlib')
datas += collect_data_files('btchip')
datas += collect_data_files('keepkeylib')
datas += collect_data_files('ckcc')

# We don't put these files in to actually include them in the script but to make the Analysis method scan them for imports
a = Analysis([home+'electrum-sibcoin',
              home+'electrum_sibcoin/gui/qt/main_window.py',
              home+'electrum_sibcoin/gui/text.py',
              home+'electrum_sibcoin/util.py',
              home+'electrum_sibcoin/wallet.py',
              home+'electrum_sibcoin/simple_config.py',
              home+'electrum_sibcoin/bitcoin.py',
              home+'electrum_sibcoin/dnssec.py',
              home+'electrum_sibcoin/commands.py',
              home+'electrum_sibcoin/plugins/cosigner_pool/qt.py',
              home+'electrum_sibcoin/plugins/email_requests/qt.py',
              home+'electrum_sibcoin/plugins/trezor/qt.py',
              home+'electrum_sibcoin/plugins/safe_t/client.py',
              home+'electrum_sibcoin/plugins/safe_t/qt.py',
              home+'electrum_sibcoin/plugins/keepkey/qt.py',
              home+'electrum_sibcoin/plugins/ledger/qt.py',
              #home+'electrum_sibcoin/plugins/coldcard/qt.py',
              #home+'packages/requests/utils.py'
              ],
             binaries=binaries,
             datas=datas,
             #pathex=[home+'lib', home+'gui', home+'plugins'],
             hiddenimports=hiddenimports,
             hookspath=[])


# http://stackoverflow.com/questions/19055089/pyinstaller-onefile-warning-pyconfig-h-when-importing-scipy-or-scipy-signal
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

# Strip out parts of Qt that we never use. Reduces binary size by tens of MBs. see #4815
qt_bins2remove=('qt5web', 'qt53d', 'qt5game', 'qt5designer', 'qt5quick',
                'qt5location', 'qt5test', 'qt5xml', r'pyqt5\qt\qml\qtquick')
print("Removing Qt binaries:", *qt_bins2remove)
for x in a.binaries.copy():
    for r in qt_bins2remove:
        if x[0].lower().startswith(r):
            a.binaries.remove(x)
            print('----> Removed x =', x)

qt_data2remove=(r'pyqt5\qt\translations\qtwebengine_locales', )
print("Removing Qt datas:", *qt_data2remove)
for x in a.datas.copy():
    for r in qt_data2remove:
        if x[0].lower().startswith(r):
            a.datas.remove(x)
            print('----> Removed x =', x)

# hotfix for #3171 (pre-Win10 binaries)
a.binaries = [x for x in a.binaries if not x[1].lower().startswith(r'c:\windows')]

pyz = PYZ(a.pure)


#####
# "standalone" exe with all dependencies packed into it

exe_standalone = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name=os.path.join('build\\pyi.win32\\electrum-sib', cmdline_name + ".exe"),
    debug=False,
    strip=None,
    upx=False,
    icon=home+'icons/electrum-sibcoin.ico',
    console=False)
    # console=True makes an annoying black box pop up, but it does make Electrum output command line commands, with this turned off no output will be given but commands can still be used

exe_portable = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas + [ ('is_portable', 'README.md', 'DATA' ) ],
    name=os.path.join('build\\pyi.win32\\electrum-sib', cmdline_name + "-portable.exe"),
    debug=False,
    strip=None,
    upx=False,
    icon=home+'icons/electrum-sibcoin.ico',
    console=False)

#####
# exe and separate files that NSIS uses to build installer "setup" exe

exe_dependent = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name=os.path.join('build\\pyi.win32\\electrum-sib', cmdline_name),
    debug=False,
    strip=None,
    upx=False,
    icon=home+'icons/electrum-sibcoin.ico',
    console=False)

coll = COLLECT(
    exe_dependent,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=None,
    upx=True,
    debug=False,
    icon=home+'icons/electrum-sibcoin.ico',
    console=False,
    name=os.path.join('dist', 'electrum'))
