import os
import setuptools
import pydustry

# Функция получения полных путей к папкам и подпапкам
def globalizer(dirpath: str) -> list:
    files = []
    folder_abspath = os.path.abspath(dirpath)
    if os.path.isdir(folder_abspath):
        for i in os.listdir(folder_abspath):
            path = folder_abspath + os.sep + i
            if os.path.isdir(path):
                for _i in globalizer(path):
                    files.append(_i)
            elif os.path.isfile(path):
                files.append(path)
    elif os.path.isfile(folder_abspath):
        files.append(folder_abspath)
    return files

setuptools.setup(
	name=pydustry.__name__,
	version=pydustry.__version__,
	description='Module for server information in the game Mindustry.',
	keywords=pydustry.__keywords__,
	packages=setuptools.find_packages(),
	author_email='semina054@gmail.com',
	url="https://github.com/romanin-rf",
	long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
	long_description_content_type="text/markdown",
	author='ProgrammerFromParlament',
	license='MIT'
)