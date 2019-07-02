from setuptools import setup

setup(name='robust_gcn',
      version='0.1',
      description='Certifiable Robustness and Robust Training for Graph Convolutional Networks',
      author='Daniel Zügner, Stephan Günnemann',
      author_email='zuegnerd@in.tum.de',
      packages=['robust_gcn'],
      install_requires=['numpy', 'scipy', 'scikit-learn', 'matplotlib', 'torch'],
      zip_safe=False)
