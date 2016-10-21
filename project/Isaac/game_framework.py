#from enum import Enum # enum class 사용 python 3.4이상



class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw

class TestGameState:
    def __init__(self, name):
        self.name = name

    #Check function call
    def enter(self):
        print('state [%s] Entered' % self.name)

    def exit(self):
        print('state [%s] Exited' % self.name)

    def pause(self):
        print("state [%s] paused" % self.name)

    def resume(self):
        print("state [%s] Resumed" % self.name)

    def handle_events(self):
        print("state [%s] handle_events" % self.name)

    def update(self):
        print("state [%s] update" % self.name)

    def draw(self):
        print("state [%s] draw" % self.name)

running = None
stack = None

def change_state(state):    #게임 상태를 state로 변화, 이전 게임 상태를 완전히 나옴
    global stack

    pop_state()
    stack.append(state)
    state.enter()

def push_state(state):      #게임 상태를 state로 변화, 이전 게임 상태는 남아 있음
    global stack

    if (len(stack) > 0):
        stack[-1].pause()

    stack.append(state)
    state.enter()

def pop_state():            #이전 게임 상태로 복귀
    global stack

    if (len(stack) > 0):
        #excute the current state's exit function, 현재 상태의 exit함수 호출
        stack[-1].exit()
        #remove the current state, 현재 상태 삭제
        stack.pop()

    #excute resume function of the previous state, 이전 상태의 resume함수 호출
    if (len(stack) > 0):
        stack[-1].resume()

def quit():                 #게임을 중단
    global running

    running = False

def run(start_state):             #게임을 state로 시작함
    global running
    global stack

    running = True
    stack = [start_state]
    start_state.enter()

    while(running):                #game-loop
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
    #repeatedly delete the top of the stack, stack의 맨 위 변수 반복 삭제
    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()

def test_game_framework():
    start_state = TestGameState('StartState')
    run(start_state)

if __name__ == '__main__':
    test_game_framework()