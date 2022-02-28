import datetime
from dataclasses import dataclass

from pgpubsub.channel import Channel, TriggerChannel
from pgpubsub.tests.models import Author, Post


@dataclass
class Reads(Channel):
    model_id: int
    model_type: str
    date: datetime.date = None


@dataclass
class PostReads(Reads):
    model_type: str = 'Post'


@dataclass
class AuthorTriggerChannel(TriggerChannel):
    model = Author


@dataclass
class PostTriggerChannel(TriggerChannel):
    model = Post
