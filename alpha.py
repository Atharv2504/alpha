import math
def alpha_beta(depth,node_index,is_maxing,scores,height,alpha,beta):
    if depth==height:
        return scores[node_index]
    
    if is_maxing:
       best=-math.inf 
       for i in range(2):
           val= alpha_beta(depth+1,node_index*2+i,False,scores,height,alpha,beta)
           best=max(best,val)
           alpha=max(alpha,best)
           if beta <= alpha:
               break
       return best
    else:
         best=math.inf
         for i in range(2):
             val=alpha_beta(depth+1,node_index*2+i,True,scores,height,alpha,beta)
             best=min(val,best)
             beta=min(beta,best)
             if beta <=alpha:
                 break
         return best
         
         
         
         
         
         
         
scores = [-1, 4, 2, 6, -3, -5, 0, 7]
height = int(math.log2(len(scores)))
print("The optimal value is :", alpha_beta(0, 0, True, scores, height, -math.inf, math.inf))
