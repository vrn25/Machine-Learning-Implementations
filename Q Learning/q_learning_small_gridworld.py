'''
####################### SMALL GRIDWORLD ###########################
    ____ ____ ____
   |    |    |    |     
   |_S__|____|____|					0,0		0,1		0,2
   |    |    |xxxx|		------>     
   |____|____|xxxx|					1,0		1,1		1,2
   |    |    |    |
   |____|____|_G__|					2,0		2,1		2,2

Actions: UP
		 DOWN
		 RIGHT
		 LEFT

Total 36 state-action pairs

Rewards: -1 for all actions in (0,0), (0,1), (1,0), (2,0)
		 -10 for going into (1,2) via any state
		 +10 for going in (2,2)

Note: State remains the same on going out of the maze (but -1 reward is given)
'''
import random
def env(state, action):
	return_val = [-1, state]

	# if next state is terminal state
	if(state[0]==2 and state[1]==1 and action==2):
		return_val = [10, [2,2]]

	# if next state is dead state
	elif(state[0]==1 and state[1]==1 and action==2):
		return_val = [-10, [1,2]]

	elif(state[0]==0 and state[1]==2 and action==1):
		return_val = [-10, [1,2]]

	else:
		# UP
		if(action==0):
			if(state[0]-1>=0):
				return_val[1] = [state[0]-1,state[1]]

		# DOWN
		if(action==1):
			if(state[0]+1<=2):
				return_val[1] = [state[0]+1,state[1]]

		# RIGHT
		if(action==2):
			if(state[1]+1<=2):
				return_val[1] = [state[0],state[1]+1]

		# LEFT
		if(action==3):
			if(state[1]-1>=0):
				return_val[1] = [state[0],state[1]-1]

	return return_val


def qlearning():
	alpha = 0.1    # step-size
	discount = 0.9 # how much do we care about immediate and future rewards
	epsilon = 0.2  # how often do we pick a random action and how often the greedy action
	num_actions = 4  # 0:up  1:down  2:right  3:left
	rows = 3
	cols = 3
	episodes = 50
	Q = [[[]for i in range(rows)] for j in range(cols)]

	print('Q values for each state-action pair before game play:')
	print('                UP	DOWN	RIGHT	LEFT')
	for i in range(rows):
		for j in range(cols):
			if(i==2 and j==2):    # goal can change accordingly when rows and columns change 
				Q[i][j][:] = [0,0,0,0]    # set initial Q value of terminal state as 0
			else:
				Q[i][j] = [random.randint(0,5) for k in range(num_actions)]   # Q value of rest of the states is a random integer
			print('state (%d, %d):        %s' %(i,j,Q[i][j]))

	print('Playing the Game %d times..........' %(episodes))

	for i in range(episodes):
		# initialize S
		currstate = [0,0]
		# loop until reach the goal state
		while(currstate!=[2,2]):
			x = currstate[0]
			y = currstate[1]
			# select A from S using epsilon greedy policy
			probability = random.random()
			if(probability>epsilon):
				curraction = Q[x][y].index(max(Q[x][y]))
			else:
				curraction = random.randint(0,num_actions-1)
			# taking action A and observing S' and R
			reward, nextstate = env(currstate, curraction)

			# perform Q learning update
			Q[x][y][curraction] = Q[x][y][curraction] + alpha * (reward + discount * (max(Q[nextstate[0]][nextstate[1]])) - Q[x][y][curraction])
			# update state
			currstate = nextstate

	print('Q values for each state-action pair after game play:')
	print('                UP	DOWN	RIGHT	LEFT')
	for i in range(rows):
		for j in range(cols):
			rounded_list = Q[i][j]
			for k in range(num_actions):
				rounded_list[k] = round(Q[i][j][k],3)
			print('state (%d, %d):        %s' %(i,j,rounded_list))

	print('Policy after self-play starting from (0,0):')

	# start state
	currstate = [0,0]
	while(currstate!=[2,2]):
		x = currstate[0]
		y = currstate[1]
		# selecting A
		curraction = Q[x][y].index(max(Q[x][y]))
		# observe S' and R
		reward, nextstate = env(currstate, curraction)
		print('Current State is (%d,%d) and immediate reward is %d' %(x,y,reward))
		# update state
		currstate  = nextstate

	print('Final State is (2,2)')

if __name__=='__main__':
	qlearning()