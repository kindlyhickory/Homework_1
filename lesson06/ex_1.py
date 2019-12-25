import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            print(self._TrafficLight__color[0])
            time.sleep(7)
            print(self._TrafficLight__color[1])
            time.sleep(2)
            print(self._TrafficLight__color[2])
            time.sleep(1)
            print(self._TrafficLight__color[1])
            time.sleep(2)


traffic_light_1 = TrafficLight()
traffic_light_1.running()
