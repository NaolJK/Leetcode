class TopVotedCandidate:
	def __init__(self, p: List[int], times: List[int]):

		count=Counter()
		maximum_vote=0
		self.recent=[]
		for i,j in enumerate(times):
			count[p[i]]+=1
			if count[p[i]]>=maximum_vote:
				maximum_vote=count[p[i]]
				self.recent.append([j,p[i]])

	def q(self, t: int) -> int:
		l=0
		r=len(self.recent)-1
		while l<=r:
			mid=l+(r-l)//2
			if self.recent[mid][0]<=t:
				ans=mid
				l=mid+1
			else:
				r=mid-1
		return self.recent[ans][1]