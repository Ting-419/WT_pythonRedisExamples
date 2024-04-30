import redis


class FullText(object):
    """
    Full text search using redis
    """

    def __init__(self):
        self.docs = ['text Simple English phrase', 'Next English text', 'Text in different language']
        self.redis = redis.Redis(host='192.168.0.106', port=6379, password='')

    def indexing(self):
        self.redis.flushall()  # clears db
        for index, doc in enumerate(self.docs):
            self.redis.hmset('docs', {index: doc})
            for word in doc.split(' '):
                self.redis.sadd(word, index)
        return self


    def find(self):
        print(self.redis.smembers('English'))  # set(['1', '0'])
        print(self.redis.smembers('text'))  # set(['1', '0'])
        print(self.redis.sunion('English', 'language'))  # OR   set(['1', '0', '2']
        print(self.redis.sinter('English', 'language'))  # AND   set([])
        print(self.redis.sinter('text', 'English'))  # AND   set(['1', '0'])
        for index in self.redis.sinter('text', 'English'):
            print(self.redis.hmget('docs', index))  # ['Next English text'] ['text Simple English phrase']

FullText().indexing().find()
