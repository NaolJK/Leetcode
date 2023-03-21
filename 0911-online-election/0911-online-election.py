class TopVotedCandidate:
	def __init__(self, p: List[int], times: List[int]):

		a=Counter()
		max_vote=0
		self.lead=[]
		for i,x in enumerate(times):
			a[p[i]]+=1
			if a[p[i]]>=max_vote:
				max_vote=a[p[i]]
				self.lead.append([x,p[i]])

	def q(self, t: int) -> int:
		l=0
		r=len(self.lead)-1
		while l<=r:
			mid=l+(r-l)//2
			if self.lead[mid][0]<=t:
				res=mid
				l=mid+1
			else:
				r=mid-1
		return self.lead[res][1]