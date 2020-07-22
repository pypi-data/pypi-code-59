#
# Copyright 2020, Xiaomi.
# All rights reserved.
# Author: huyumei@xiaomi.com
#
from talos.thrift.auth.ttypes import Credential
from talos.client.TalosClientFactory import MessageClient
from talos.client.TalosClientFactory import ConsumerClient
from talos.client.TalosClientFactory import TopicClient
import logging


class TalosAdmin(object):
    logger = logging.getLogger("TalosAdmin")
    topicClient = TopicClient
    messageClient = MessageClient
    consumerClient = ConsumerClient
    credential = Credential()

    def __init__(self, talosClientFactory=None):
        self.topicClient = talosClientFactory.new_topic_client()

    # topicAttribute for partitionNumber required

    def get_describe_info(self, request=None):
        return self.topicClient.get_describe_info(request)

    def get_topic_attribute(self, request=None):
        return self.topicClient.get_topic_attribute(request)

