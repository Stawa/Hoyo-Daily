from setuptools import setup, find_packages

f = open("README.md", "r", encoding="utf-8")
README = f.read()

setup(
    name="Hoyo-Daily",
    version="1.0.2",
    packages=find_packages(),
    install_requires=["genshin", "discord-webhook", "pytz", "requests"],
    license="MIT",
    url="https://github.com/Stawa/Hoyo-Daily",
    project_urls={
        "Source": "https://github.com/Stawa/Hoyo-Daily",
        "Tracker": "https://github.com/Stawa/Hoyo-Daily/issues",
    },
    author="Stawa",
    description="Automatic HoyoLab Daily Check-in with Python",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=["hoyolab", "genshin impact", "honkai3rd", "daily-checkin"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
)
