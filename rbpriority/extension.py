# rbpriority Extension for Review Board.

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import ReviewRequestFieldsHook
from reviewboard.reviews.fields import BaseEditableField

from enum import IntEnum
import string

Priority = IntEnum(b'Priority', b'low normal high')


class PriorityField(BaseEditableField):
    fieldset_id = 'priority'
    label = 'Priority'

    def load_value(self, review_requests_details):
        priority = (super(PriorityField, self).load_value(review_requests_details)
                      or Priority.normal)
        return string.capwords(priority.name)

class PriorityExtension(Extension):
    metadata = {
        'Name': 'rbpriority',
        'Summary': 'Describe your extension here.',
    }

    def initialize(self):
        ReviewRequestFieldsHook(self, 'info', [PriorityField])
