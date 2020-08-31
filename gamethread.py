import threading
import random
import time


class GameThread(threading.Thread):
    game = None

    def __init__(self, game):
        threading.Thread.__init__(self)
        self.game = game

    def run(self):
        time_step = (1000 / self.game.fps) / 1000
        step_counter = 0
        while self.game.running:
            start_time = time.time()
            step_counter += 1

            if step_counter % self.game.fps == 0:
                step_counter = 0
                self.game.actual_frame_rate = self.game.frame_rate_counter
                self.game.frame_rate_counter = 0

            if step_counter % (self.game.fps / 2) == 0:
                if not self.game.waiting:
                    self.game.update_score()

            j = 0
            while j < len(self.game.random_color):
                self.game.random_color[j] += (j + 1) * 10
                if self.game.random_color[j] > 255:
                    self.game.random_color[j] = 0
                j += 1

            if self.game.gameover:
                self.game.game_over_animation()

            if self.game.hit > 0:
                self.game.hit -= 1

            self.game.update_game()
            self.game.event_handling()

            time_passed = time.time() - start_time
            sleep_time = time_step - time_passed
            if(sleep_time < 0):
                sleep_time = 0
            time.sleep(sleep_time)
