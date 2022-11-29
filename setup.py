import setuptools

with open("README.md", "r") as fh:
    long_description: str = fh.read()

setuptools.setup(
    name='base114514',
    version='0.4',
    script="base114514.py",
    author="Yidaozhan Ya",
    author_email="ydz@yidaozhan.top",
    maintainer="Yidaozhan Ya",
    maintainer_email="ydz@yidaozhan.top",
    description="Base114514 encoding, the algorithm from Shimokitazawa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YidaozhanYa/base114514",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts': ['base114514 = base114514:main']},
    keywords=['base114514', 'base64'],
    python_requires='>=3.10',
    zip_safe=False,
    include_package_data=True,
)
