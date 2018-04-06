list_of_papers=[100,50,10,5,2,1]
total_mony=500
request=950

def give_Money(req):
	given=""
	i=0
	if req > total_mony:
		return "your request is greater than total_mony in ATM"
	while req> 0:
		div=req/list_of_papers[i]
		given+="give "+str (div)+ ' of '+str (list_of_papers[i])+" $ \n"
		req=req- div * list_of_papers[i]
		i+=1
	return given

print give_Money(request)


