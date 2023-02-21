from setuptools import setup

setup(
        name='CyberKernel',
        version='0.0.9',
        description='A django based blog management project',
        author='Dev-Bittu',
        author_email='devbittu@proton.me',
        url='github.com/Dev-Bittu/CyberKernel',
        download_url='https://github.com/Dev-Bittu/CyberKernel/archive/refs/heads/main.zip',
        license_files='LICENSE',
        project_urls=['https://github.com/Dev-Bittu/CyberKernel'],
        packages=['cyberkernel'],
        install_requires=[
            'django',
            'pillow',
            'tzdata',
            'django-ckeditor',
        ],
        long_description = 'A django based blog management project, made & maintained by Dev-Bittu'
)
