import zmq
import Leap
import time

broadcastMSG = "None"

class SampleListener(Leap.Listener):
    def on_frame(self, controller):
        frame = controller.frame()
        hands = frame.hands
        normalPalmPos = hands[0].palm_normal
        palmPos = hands[0].palm_position
        if (hands[0].is_valid):
            pwm = palmPos.y / 6.5

            if (pwm >= 100):
                pwm = 99

            if(normalPalmPos.x > 0):
                global broadcastMSG
                broadcastMSG = "CW:" + str(int(pwm))
            else:
                global broadcastMSG
                broadcastMSG = "CC:" + str(int(pwm))

if __name__ == "__main__":
    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    ctx = zmq.Context.instance()
    publisher = ctx.socket(zmq.PUB)
    publisher.bind("tcp://*:9999")
    counter = 0
    lastMessage = "lastMessage"
    while(1):
        if(lastMessage != broadcastMSG):
            publisher.send_string(broadcastMSG)
            print("Broadcast Message " + str(counter) + " : " + broadcastMSG)
            lastMessage = broadcastMSG
            counter += 1
            time.sleep(0.05)

    controller.removeListener(listener)