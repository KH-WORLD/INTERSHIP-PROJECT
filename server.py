from SimpleXMLRPCServer import SimpleXMLRPCServer
import RPi.GPIO as GPIO

# GPIO Configuration 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)


def verin1_on():
    print ("verin1 up")
    GPIO.output(18,GPIO.HIGH)
    return True
def verin1_off():
    print ("verin 1 down")
    GPIO.output(18,GPIO.LOW)
    return True
##################################
def verin2_on():
    print ("verin 2 up")
    GPIO.output(14,GPIO.HIGH)
    return True

def verin2_off():
    print ("verin 2 down")
    GPIO.output(14,GPIO.LOW)
    return True
##################################
def verin3_on():
    print ("verin 3 up")
    GPIO.output(15,GPIO.HIGH)
    return True

def verin3_off():
    print ("verin 3 down")
    GPIO.output(15,GPIO.LOW)
    return True
####################################
def verin4_on():
    print ("verin 4 up")
    GPIO.output(23,GPIO.HIGH)
    return True

def verin4_off():
    print ("verin 4 down")
    GPIO.output(23,GPIO.LOW)
    return True
########################################
def verin5_on():
    print ("verin 5 up")
    GPIO.output(24,GPIO.HIGH)
    return True

def verin5_off():
    print ("verin 5 down")
    GPIO.output(24,GPIO.LOW)
    return True

##########################################
def verin6_on():
    print ("verin 6 up")
    GPIO.output(25,GPIO.HIGH)
    return True

def verin6_off():
    print ("verin 6 down")
    GPIO.output(25,GPIO.LOW)
    return True
#######################################
#######################################
def effet1_on():
    print ("effet 1 run")
    GPIO.output(8,GPIO.HIGH)
    return True

def effet1_off():
    print ("effet 1 stop")
    GPIO.output(8,GPIO.LOW)
    return True
#######################################
def effet2_on():
    print ("effet 2 run")
    GPIO.output(7,GPIO.HIGH)
    return True
def effet2_off():
    print ("effet 2 stop")
    GPIO.output(7,GPIO.LOW)
    return True
##########################################
def effet3_on():
    print ("effet 3 run")
    GPIO.output(12,GPIO.HIGH)
    return True

def effet3_off():
    print ("effet 3 stop")
    GPIO.output(12,GPIO.LOW)
    return True
###################### les scenario #########################

def scenario_up():
	verin1_on()
	verin2_on()
	verin3_on()
        verin4_on()
	verin5_on()
	verin6_on()
        return True
def scenario_down():
	verin1_off()
	verin2_off()
	verin3_off()
	verin4_off()
	verin5_off()
	verin6_off()
        return True

def scenario_right():
	verin1_on()
	verin2_on()
	verin3_off()
	verin4_off()
	verin5_off()
	verin6_off()
        return True



def scenario_left():
	verin1_off()
	verin2_off()
	verin3_off()
	verin4_off()
	verin5_on()
	verin6_on()
	return True

def scenario_front():
        verin1_on()
        verin2_off()
        verin3_off()
        verin4_off()
        verin5_off()
        verin6_on()
        return True


def scenario_back():
        verin1_on()
        verin2_on()
        verin3_off()
        verin4_off()
        verin5_on()
        verin6_on()
        return True


server = SimpleXMLRPCServer(("192.168.1.11",8000))
print "Listening on port 8000..."
server.register_function(scenario_up, "scenario_up")
server.register_function(scenario_down, "scenario_down")
server.register_function(scenario_right,"scenario_right")
server.register_function(scenario_left, "scenario_left")
server.register_function(scenario_front,"scenario_front")
server.register_function(scenario_back, "scenario_back")
#server.register_function(verin1_on, "verin1_on")
#server.register_function(verin1_off, "verin1_off")
#server.register_function(verin2_on, "verin2_on")
#server.register_function(verin2_off, "verin2_off")
server.serve_forever()

