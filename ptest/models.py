from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible



class Question(models.Model):
    question = models.TextField()
    description = models.CharField(max_length=500, blank=True)

    def count_choices(self):
        return self.choice_set.count()

    def count_total_votes(self):
        result = 0
        for choice in self.choice_set.all():
            result += choice.count_votes()
        return result

    def can_vote(self, user):
        return not self.vote_set.filter(user=user).exists()

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice = models.CharField(max_length=500)

    def count_votes(self):
        return self.vote_set.count()

    def __unicode__(self):
        return self.choice

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.choice


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(Question)
    choice = models.ForeignKey(Choice)

    def __unicode__(self):
        return u'Vote for %s' % (self.choice)

    class Meta:
        unique_together = (('user', 'question'))

    def __str__(self):
        return str(self.user.id)+'-' + str(self.question.id)+'-' + self.choice.choice