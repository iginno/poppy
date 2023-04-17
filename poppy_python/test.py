from pypot.creatures import PoppyHumanoid
from pypot.primitive.move import MoveRecorder, MovePlayer
import logging, sys, time
logging.basicConfig(stream=sys.stderr, level="INFO")
poppy = PoppyHumanoid(config="/opt/iginno/poppy_python/configuration/poppy_humanoid.json")
#poppy.sit_position.start()
#poppy.limit_torque.stop()
# poppy.stand_position.start()
# time.sleep(5)
# poppy.stand_position.stop()
# for m in poppy.arms:
#     m.compliant = True
# # m_value = [0]*25
# # b_print = False
# # while(True):
# #     for i in range(25):
# #         if m_value[i] != poppy.motors[i].present_position:
# #             m_value[i]=poppy.motors[i].present_position
# #             b_print = True
# #         else:
# #             b_print = False
# #     if b_print:
# #         print (m_value)
# #     else:
# #         print("nothing changed")
# #     time.sleep(0.1)


# # for m in poppy.motors:
# #     m.compliant = True
# record = MoveRecorder(poppy, 20, poppy.motors)
# # Give you time to get ready
# print('Get ready to record a move...')
# time.sleep(5)

# # Start the record
# record.start()
# print('Now recording !')

# # Wait for 10s so you can record what you want
# time.sleep(10)

# # Stop the record
# print('The record is over!')
# record.stop()

# my_recorded_move = record.move
# player = MovePlayer(poppy, my_recorded_move)

# for _ in range(5):
#     player.start()
#     player.wait_to_stop()
input("wait for enter key......")
