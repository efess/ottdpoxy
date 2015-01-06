# Simple publish/subscribe event system
class PubSub:
    __subscriptions = {}

    @staticmethod
    def subscribe(topic, func):
        if not topic in PubSub.__subscriptions:
            PubSub.__subscriptions[topic] = [func]
        else:
            PubSub.__subscriptions[topic].append(func)

    @staticmethod
    def publish(topic, data):
        if topic in PubSub.__subscriptions:
            for func in PubSub.__subscriptions[topic]:
                func(data)