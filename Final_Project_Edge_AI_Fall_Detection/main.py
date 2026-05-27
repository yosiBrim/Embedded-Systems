import time
from pose_engine import PoseEngine

class FallDetectionSystem:
    def __init__(self):
        self.engine = PoseEngine()
        print("System Initialized.")

    def run(self):
        while True:
            self.engine.detect_fall(None)
            time.sleep(2)

if __name__ == "__main__":
    system = FallDetectionSystem()
    system.run()
