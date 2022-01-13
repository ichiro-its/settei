from setuptools import setup

package_name = 'settei'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools'
    ],
    zip_safe=True,
    maintainer='Segara Bhagas Dagsapurwa',
    maintainer_email='segara2410@gmail.com',
    description='Configuration server project',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = settei.main:main',
        ],
    },
)
