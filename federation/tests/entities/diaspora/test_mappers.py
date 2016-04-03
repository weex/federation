# -*- coding: utf-8 -*-
from datetime import datetime

from federation.entities.base import Post
from federation.entities.diaspora.mappers import message_to_objects
from federation.tests.fixtures.payloads import DIASPORA_POST_SIMPLE


class TestDiasporaEntityMappersReceive(object):

    def test_message_to_objects_simple_post(self):
        entities = message_to_objects(DIASPORA_POST_SIMPLE)
        assert len(entities) == 1
        post = entities[0]
        assert isinstance(post, Post)
        assert post.raw_content == "((status message))"
        assert post.guid == "((guid))"
        assert post.handle == "alice@alice.diaspora.example.org"
        assert post.public == False
        assert post.created_at == datetime(2011, 7, 20, 1, 36, 7)
