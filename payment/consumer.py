import time

from main import redis, Order

key = 'refund_order'
group = 'payment-group'

try:
    # create consumer group if it doesn't exist
    redis.xgroup_create(key, group)
except:
    print("Group already exists")

while True:
    try:
        # read data from stream, every 1 second we will consume messages
        results = redis.xreadgroup(group, key, {key: '>'}, None)

        if results != []:
            print(results)
            for result in results:
                obj = result[1][0][1]
                order = Order.get(obj['pk'])
                order.status = 'refunded'
                order.save()
    except Exception as e:
        print(str(e))
    time.sleep(1)
