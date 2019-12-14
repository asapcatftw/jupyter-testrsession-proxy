import setuptools

setuptools.setup(
    name="jupyter-testrsession-proxy",
    version='1.0dev',
    url="https://github.com/sanjaydatasciencedojo/jupyter-rsession-proxy",
    author="Ryan Lovett & Yuvi Panda",
    description="Jupyter extension to proxy RStudio's rsession",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'shiny = jupyter_rsession_proxy:setup_testshiny'
        ]
    },
    package_data={
        'jupyter_rsession_proxy': ['icons/*'],
    },
)
