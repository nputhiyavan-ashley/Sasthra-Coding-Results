import sys
from collections import deque
def sliding_window():
    inptokens=sys.stdin.read().split()
    if len(inptokens)<2:
        return
    tot_elem=int(inptokens[0])
    win_capacity=int(inptokens[1])
    raw_elem=inptokens[2:2+tot_elem]
    mbers=[float(item) for item in raw_elem]
    if win_capacity>tot_elem or win_capacity<=0 or tot_elem==0:
        return
    run_sum=0.0
    dec_deque=deque()
    avg=0.0
    for idx in range(tot_elem):
        run_sum+=mbers[idx]
        if idx>=win_capacity:
            run_sum-=mbers[idx-win_capacity]
        while dec_deque and mbers[dec_deque[-1]] <=mbers[idx]:
            dec_deque.pop()
        dec_deque.append(idx)
        if dec_deque[0]<=idx-win_capacity:
            dec_deque.popleft()
        if idx>=win_capacity-1:
            avg=run_sum/win_capacity
            sys.stdout.write(f"{avg:.2f},{raw_elem[dec_deque[0]]}\n")        
if __name__=="__main__":
    sliding_window()
    
