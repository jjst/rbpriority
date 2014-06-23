from reviewboard.extensions.packaging import setup


PACKAGE = "rbpriority"
VERSION = "0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="Extension rbpriority",
    author="Jeremie Jost",
    packages=["rbpriority"],
    entry_points={
        'reviewboard.extensions':
            '%s = rbpriority.extension:PriorityExtension' % PACKAGE,
    },
    package_data={
        'rbpriority': [
            'templates/rbpriority/*.txt',
            'templates/rbpriority/*.html',
        ],
    },
    scripts=['bin/rb-priority-alert'],
    install_requires=[
        'enum34'
        ]
)
