"""

    taggable.managers
    -----------------

    Django managers.

    :copyright: 2010 by Gustavo Picon
    :license: Apache License 2.0

"""

from django.db import models
from taggable.querysets import TaggedQuerySet, EmptyTaggedQuerySet


class TaggedManager(models.Manager):
    """ Manager for the Tagged abstract class.
    """

    def _kwargs(self):
        try:
            return {'using': self._db}
        except AttributeError:
            return {}

    def get_empty_query_set(self):
        """ TODO: docstring
        """
        return EmptyTaggedQuerySet(self.model, **self._kwargs())

    def get_query_set(self):
        """ TODO: docstring
        """
        return TaggedQuerySet(self.model, **self._kwargs())
