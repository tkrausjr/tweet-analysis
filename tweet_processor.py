from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient
import os


access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret =  os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
consumer_key =  os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret =  os.environ["TWITTER_CONSUMER_SECRET"]
twitter_filter = os.environ["TWITTER_FILTER_STRING"]
kafka_target = os.environ["KAFKA_TARGET"]  # IP Address : Port IE - 10.10.1.11:9092

print("Access Token " + access_token)
print("Access Token Secret " + access_token_secret)
print("Consumer Key " + consumer_key)
print("Consumer Secret " + consumer_secret)
print("KAFKA Target " + kafka_target)


class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("test", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient(kafka_target)
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=twitter_filter)