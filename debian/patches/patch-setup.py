Index: Electrum-SIBCOIN-3.2.3/setup.py
===================================================================
--- Electrum-SIBCOIN-3.2.3.orig/setup.py
+++ Electrum-SIBCOIN-3.2.3/setup.py
@@ -77,6 +77,7 @@ setup(
         'electrum_sibcoin',
         'electrum_sibcoin.gui',
         'electrum_sibcoin.gui.qt',
+        'electrum_sibcoin.plugins',
     ] + [('electrum_sibcoin.plugins.'+pkg) for pkg in find_packages('electrum_sibcoin/plugins')],
     package_dir={
         'electrum_sibcoin': 'electrum_sibcoin'
