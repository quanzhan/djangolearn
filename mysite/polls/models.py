from django.utils.translation import ugettext as _
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Poll(models.Model):
    name = models.CharField(_('name'), max_length=80)
    question = models.CharField(_('question'), max_length=80)
    pub_date = models.DateTimeField(_('pub_date'))
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        now = timezone.now()
        return now > self.pub_date >= now - datetime.timedelta(days=1)
class Choice(models.Model):
    name = models.CharField(_('name'), max_length=80)
    poll = models.ForeignKey(Poll)
    def __unicde__(self):
        return self.name
