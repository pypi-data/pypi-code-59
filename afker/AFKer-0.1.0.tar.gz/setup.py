from setuptools import setup, find_packages

setup (
        name='AFKer',
        version='0.1.0',
        description='AFK script',
        url='https://github.com/LiamMcFadden/AFKer',
        author='Liam McFadden',
        author_email='liamm18@vt.edu',
        keywords='afk video games',
        packages=find_packages(),
        install_requires=['keyboard', 'pyautogui'],
        python_requires='>=3.6',
)
