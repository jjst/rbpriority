from __future__ import unicode_literals

def include_enabled_extensions(settings):
    """
    This adds enabled extensions to the INSTALLED_APPS cache
    so that operations like syncdb and evolve will take extensions
    into consideration.
    """
    from django.db.models.loading import load_app
    from django.db import DatabaseError

    from reviewboard.extensions.base import get_extension_manager

    try:
        manager = get_extension_manager()
    except DatabaseError:
        # This database is from a time before extensions, so don't attempt to
        # load any extensions yet.
        return

    for extension in manager.get_enabled_extensions():
        load_app(extension.info.app_name)

def get_high_priority_reviews():
    pass

def send_email_reminder(reviews):
    pass

def main(in_subprocess):
    # Some of our checks require access to django.conf.settings, so
    # tell Django about our settings.
    #
    # Initialize Review Board, so we're in a state ready to load
    # extensions and run management commands.
    from reviewboard import settings, initialize
    initialize()

    include_enabled_extensions(settings)

    high_priority_reviews = get_high_priority_reviews()

    send_email_reminder(high_priority_reviews)

