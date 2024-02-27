import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

setuptools.setup(
    name="pytvm",
    version="0.0.1",
    author="Maksim Kurbatov",
    author_email="cyrbatoff@gmail.com",
    description="Python TVM emulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages('.', exclude=['.idea', 'tests', 'examples']),
    package_data={'pytvm': ['engine/**/*']},
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries",
    ],
    url="https://github.com/yungwine/pytvm",
    python_requires='>=3.9',
    py_modules=["pyraptorq"],
    cmdclass={'bdist_wheel': bdist_wheel},
)
