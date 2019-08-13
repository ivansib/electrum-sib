from pythonforandroid.recipe import CythonRecipe


class X11HashRecipe(CythonRecipe):

    url = 'https://github.com/TriKriSta/x11_hash/archive/master.zip'
    version = '1.4.1'
    depends = ['python3', 'setuptools']

    def should_build(self, arch):
        """It's faster to build than check"""
        return True


recipe = X11HashRecipe()
