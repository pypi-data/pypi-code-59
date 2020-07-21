START_URLS_TOPIC = 'start-topic-{}'

SCHEDULER_DUPEFILTER_KEY = '{}:dupefilter'
SCHEDULER_DUPEFILTER_CLASS = 'kafka_scrapy.dupefilter.RFPDupeFilter'
REDIS_PARAMS = {
    'socket_timeout': 30,
    'socket_connect_timeout': 30,
    'retry_on_timeout': True,
    'encoding': 'utf-8',
}

DUPEFILTER_KEY = 'dupefilter:%(timestamp)s'

SCHEDULER_QUEUE_CLASS = 'kafka_scrapy.queues.KafkaQueue'
KAFKA_DEFAULTS_HOST = 'localhost:9092'
KAFKA_DEFAULTS_TOPIC = 'topic-{}'
BLOOMFILTER_BLOCK = 1
BLOOMFILTER_SIZE = 31
BLOOMFILTER_SEED = 6
