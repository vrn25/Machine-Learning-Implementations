'''
####################### GRIDWORLD ###########################
    GridWorld like:

    T o o ..........o
    o o o ..........o
    . .             .        
    . .             .  
    . .             o
    . .             o
    o o o ......o o T
Actions: 
     UP (0)
		 DOWN (1)
		 RIGHT (2)
		 LEFT (3)

Rewards: 
		 0 once the agent reaches Terminal state
    -1 for all other actions in any state

Note: State remains the same on going out of the maze (but -1 reward is given)
'''
def env(state, action, rows, columns):
	# return_val = [prob, next state, reward, isdone]
  num_states = rows * columns
  isdone = lambda state: state==0 or state==(num_states-1)
  reward = lambda state: 0 if isdone(state) else -1

  if(isdone(state)):
    next_state = state
  else:
    if(action==0):
      next_state = state-columns if state-columns>=0 else state
    elif(action==1):
      next_state = state+columns if state+columns<num_states else state
    elif(action==2):
      next_state = state+1 if (state+1)%columns else state
    elif(action==3):
      next_state = state-1 if state%columns else state 
      
  return_val = [1, next_state, reward(state), isdone(next_state)]
  return return_val