
#Initial Password Input

def passwordsetup():
	from getpass import getpass as gp

	passmatch = False
	passcount = 0
	passfinal = ""

	while not passmatch and passcount < 3:

	    password_try1 = gp()
	    password_try2 = gp()

	    if password_try1 == password_try2:
	    	print "Your password has been set"
	    	passfinal = password_try2
	        passmatch = True
	    elif passcount < 2:
	        print "Sorry, those passwords did not match, try again"
	        passcount = passcount + 1
	    else:
	    	print "Sorry, you clearly can't type. go home."

	return passfinal