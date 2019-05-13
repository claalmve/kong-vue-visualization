from collections import OrderedDict
from datetime import timedelta, datetime
import random


'''
Ideally, we would like to hire someone with strong design and front end programming skills,
capable of exposing in charts information that would otherwise be hidden, or at least not explicit,
in data sets.

As such we want to evaluate the candidates skills on presenting data in meaningful graphs.
We are not only interested in the candidate ability to implement the front end applications that
would present the graphs, we are also interested in the rationale behind the decisions.

The more hidden (or not explicit) meaningful information becomes evident in graphs the better.

Values:
    1. Autonomous action: We are a young team with no product manager.
       We need individuals who can go make important decisions by themselves and do the work
       needed to know that those decisions are the best way forward on their own.
    2. Communication: We are a remote team.  We require teammates who communicate themselves and
       their ideas well, and are fastidious about keeping online communication open.
    3. Innovation + Reflection: We want our team to always be striving to do the best.
       To achieve that, our members must be innovative in their solutions, and reflective about
       their innovations.


Project Description

Implement an app or widget to present visual information from a dataset of http requests

Project Purpose

To evaluate the ability to present useful information from a dataset in meaningful graphs.

Dependencies

Please write this project using vue.js.
We provide a CSV file containing the data required. It consists of 100k lines, each representing one
http request. Each line has request_time, service_name, http_method, consumer_id, latency_in_seconds
and response_code as columns.


'''


def generate_traffic_data(number_of_services, number_of_consumers, number_of_requests, start):
    methods = OrderedDict([('get', 0.2), ('post', 0.8)])
    response_codes = OrderedDict([('200', 0.8), ('500', 0.1), ('401', 0.1)])
    consumers = [f'consumer_{i}' for i in range(number_of_consumers)]
    services = [f'service_{i}' for i in range(number_of_consumers)]
    latencies_models = (
        lambda: random.gauss(0.01, 0.001),
        lambda: random.gauss(1, 0.0012),
        lambda: random.gauss(5, 0.1),
        lambda: random.randrange(5, 8, 1),
    )
    latencies_models_probabilities = (0.7, 0.2, 0.05, 0.05)
    last_time = start

    for i in range(number_of_requests):
        interval = random.randrange(0, 100, 1) * 0.05  # maximum interval between requests: 5s
        last_time = last_time + timedelta(seconds=interval)
        method = random.choices(list(methods.keys()), list(methods.values()))[0]
        consumer = random.choice(consumers)
        response = random.choices(list(response_codes.keys()), list(response_codes.values()))[0]
        service = random.choice(services)
        latency_model = random.choices(latencies_models, latencies_models_probabilities, k=1)[0]
        latency = latency_model()

        yield f'{last_time},{service},{method},{consumer},{latency},{response}\n'


if __name__ == '__main__':
    columns = 'request_time,service_name,http_method,consumer_id,latency_in_seconds,response_code\n'
    with open('traffic.csv', 'w') as f:
        f.write(columns)
        for line in generate_traffic_data(10, 5000, 100000, datetime(2017, 1, 1)):
            f.write(line)
