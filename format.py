dict={'deposit':0,'withdraw':0,'total':0};
ch=0;d=0;w=0;
while ch!="e":
	ch=input("enter d to deposit and w to withdraw and e to exit:");
	if ch=="d":
		amt=int(input("enter amount:"));
		dict["deposit"] +=amt;
		dict["total"]+=amt;
		print(dict);
	elif ch=="w":
		if dict["total"]==0:
			print("cannot withdraw");
		else:		
			amt=int(input("enter amount:"));
			dict["withdraw"] +=amt;
			dict["total"]-=amt;
			if dict["total"]<0:
				print("cannot withdraw unsufficient balance");
			else:
				print(dict);
	


