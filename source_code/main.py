from agent import Qnet
from agent import ReplayBuffer
from agent import train 


q = Qnet()
q_target = Qnet()
q_target.load_state_dict(q.state_dict())
memory = ReplayBuffer()

print_interval = 20
score = 0.0  
optimizer = optim.Adam(q.parameters(), lr=learning_rate)
score_history= []
for n_epi in range(3000):
    epsilon = max(0.01, 0.08 - 0.01*(n_epi/200)) #Linear annealing from 8% to 1%
    s = env.reset(random_init=True)
    done = False
    n_step =0 
    while not done:
        n_step +=1
        a = q.sample_action(torch.from_numpy(np.array(s)).float(), epsilon)      
        s_prime, r, done = env.transition(a)
        done_mask = 0.0 if done else 1.0
        memory.put((s,a,r,s_prime, done_mask))

        score += r
        if done:
            break
        s = s_prime
        
    if memory.size()>2000:
        train(q, q_target, memory, optimizer)

    if n_epi%print_interval==0 and n_epi!=0:
        q_target.load_state_dict(q.state_dict())
        print("n_episode :{}, score : {:.1f}, n_buffer : {}, eps : {:.1f}%, n_step:{}".format(n_epi, score/print_interval, memory.size(), epsilon*100, n_step))
        score_history.append(score/print_interval)
        score = 0.0