from ev3dev2.power import PowerSupply
from ev3dev2.sensor import Sensor
from ev3dev2.sensor.lego import TouchSensor, GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.motor import Motor, LargeMotor, MediumMotor
from ev3dev2.port import LegoPort
import requests
import json

def ev3(api_key):
    if (LegoPort('in1').status == 'no-sensor'):
        input_port_1_driver_name = ''
        input_port_1_value = ''
    else:
        if Sensor('in1').driver_name == 'lego-ev3-touch':
            input_port_1 = TouchSensor('in1')
            input_port_1_driver_name = Sensor('in1').driver_name
            input_port_1_value = input_port_1.is_pressed
        elif Sensor('in1').driver_name == 'lego-ev3-gyro':
            input_port_1 = GyroSensor('in1')
            #input_port_1.reset()
            input_port_1_driver_name = Sensor('in1').driver_name
            input_port_1_value = input_port_1.angle
        elif Sensor('in1').driver_name == 'lego-ev3-us': 
            input_port_1 = UltrasonicSensor('in1')
            input_port_1_driver_name = Sensor('in1').driver_name
            input_port_1_value = input_port_1.distance_centimeters
        elif Sensor('in1').driver_name == 'lego-ev3-color': 
            input_port_1 = ColorSensor('in1')
            input_port_1_driver_name = Sensor('in1').driver_name
            input_port_1_value = input_port_1.color
        else:
            input_port_1_driver_name = ''
            input_port_1_value = ''

    if (LegoPort('in2').status == 'no-sensor'):
        input_port_2_driver_name = ''
        input_port_2_value = ''
    else:
        if Sensor('in2').driver_name == 'lego-ev3-touch':
            input_port_2 = TouchSensor('in2')
            input_port_2_driver_name = Sensor('in2').driver_name
            input_port_2_value = input_port_2.is_pressed
        elif Sensor('in2').driver_name == 'lego-ev3-gyro':
            input_port_2 = GyroSensor('in2')
            #input_port_2.reset()
            input_port_2_driver_name = Sensor('in2').driver_name
            input_port_2_value = input_port_2.angle
        elif Sensor('in2').driver_name == 'lego-ev3-us': 
            input_port_2 = UltrasonicSensor('in2')
            input_port_2_driver_name = Sensor('in2').driver_name
            input_port_2_value = input_port_2.distance_centimeters
        elif Sensor('in2').driver_name == 'lego-ev3-color': 
            input_port_2 = ColorSensor('in2')
            input_port_2_driver_name = Sensor('in2').driver_name
            input_port_2_value = input_port_2.color
        else:
            input_port_2_driver_name = ''
            input_port_2_value = ''
            
    if (LegoPort('in3').status == 'no-sensor'):
        input_port_3_driver_name = ''
        input_port_3_value = ''
    else:
        if Sensor('in3').driver_name == 'lego-ev3-touch':
            input_port_3 = TouchSensor('in3')
            input_port_3_driver_name = Sensor('in3').driver_name
            input_port_3_value = input_port_3.is_pressed
        elif Sensor('in3').driver_name == 'lego-ev3-gyro':
            input_port_3 = GyroSensor('in3')
            #input_port_3.reset()
            input_port_3_driver_name = Sensor('in3').driver_name
            input_port_3_value = input_port_3.angle
        elif Sensor('in3').driver_name == 'lego-ev3-us': 
            input_port_3 = UltrasonicSensor('in3')
            input_port_3_driver_name = Sensor('in3').driver_name
            input_port_3_value = input_port_3.distance_centimeters
        elif Sensor('in3').driver_name == 'lego-ev3-color': 
            input_port_3 = ColorSensor('in3')
            input_port_3_driver_name = Sensor('in3').driver_name
            input_port_3_value = input_port_3.color
        else:
            input_port_3_driver_name = ''
            input_port_3_value = ''

    if (LegoPort('in4').status == 'no-sensor'):
        input_port_4_driver_name = ''
        input_port_4_value = ''
    else:
        if Sensor('in4').driver_name == 'lego-ev3-touch':
            input_port_4 = TouchSensor('in4')
            input_port_4_driver_name = Sensor('in4').driver_name
            input_port_4_value = input_port_4.is_pressed
        elif Sensor('in4').driver_name == 'lego-ev3-gyro':
            input_port_4 = GyroSensor('in4')
            #input_port_4.reset()
            input_port_4_driver_name = Sensor('in4').driver_name
            input_port_4_value = input_port_4.angle
        elif Sensor('in4').driver_name == 'lego-ev3-us': 
            input_port_4 = UltrasonicSensor('in4')
            input_port_4_driver_name = Sensor('in4').driver_name
            input_port_4_value = input_port_4.distance_centimeters
        elif Sensor('in4').driver_name == 'lego-ev3-color': 
            input_port_4 = ColorSensor('in4')
            input_port_4_driver_name = Sensor('in4').driver_name
            input_port_4_value = input_port_4.color
        else:
            input_port_4_driver_name = ''
            input_port_4_value = ''

    if (LegoPort('outA').status == 'no-motor'):
        output_port_a_driver_name = ''
        output_port_a_value = ''
    else:
        if Motor('outA').driver_name == 'lego-ev3-l-motor':
            output_port_a = LargeMotor('outA')
            output_port_a_driver_name = Motor('outA').driver_name
            output_port_a_value = output_port_a.position
        elif Motor('outA').driver_name == 'lego-ev3-m-motor':
            output_port_a = MediumMotor('outA')
            output_port_a_driver_name = Motor('outA').driver_name
            output_port_a_value = output_port_a.position
        else:
            output_port_a_driver_name = ''
            output_port_a_value = ''

    if (LegoPort('outB').status == 'no-motor'):
        output_port_b_driver_name = ''
        output_port_b_value = ''
    else:
        if Motor('outB').driver_name == 'lego-ev3-l-motor':
            output_port_b = LargeMotor('outB')
            output_port_b_driver_name = Motor('outB').driver_name
            output_port_b_value = output_port_b.position
        elif Motor('outB').driver_name == 'lego-ev3-m-motor':
            output_port_b = MediumMotor('outB')
            output_port_b_driver_name = Motor('outB').driver_name
            output_port_b_value = output_port_b.position
        else:
            output_port_b_driver_name = ''
            output_port_b_value = ''

    if (LegoPort('outC').status == 'no-motor'):
        output_port_c_driver_name = ''
        output_port_c_value = ''
    else:
        if Motor('outC').driver_name == 'lego-ev3-l-motor':
            output_port_c = LargeMotor('outC')
            output_port_c_driver_name = Motor('outC').driver_name
            output_port_c_value = output_port_c.position
        elif Motor('outC').driver_name == 'lego-ev3-m-motor':
            output_port_c = MediumMotor('outC')
            output_port_c_driver_name = Motor('outC').driver_name
            output_port_c_value = output_port_c.position
        else:
            output_port_c_driver_name = ''
            output_port_c_value = ''

    if (LegoPort('outD').status == 'no-motor'):
        output_port_d_driver_name = ''
        output_port_d_value = ''
    else:
        if Motor('outD').driver_name == 'lego-ev3-l-motor':
            output_port_d = LargeMotor('outD')
            output_port_d_driver_name = Motor('outD').driver_name
            output_port_d_value = output_port_d.position
        elif Motor('outD').driver_name == 'lego-ev3-m-motor':
            output_port_d = MediumMotor('outD')
            output_port_d_driver_name = Motor('outD').driver_name
            output_port_d_value = output_port_d.position
        else:
            output_port_d_driver_name = ''
            output_port_d_value = ''

    x = requests.put('https://urthings.io/api/devices/' + api_key, data = {'battery_level': PowerSupply().measured_volts, 'brick_name': brick_name,'input_port_1': input_port_1_driver_name, 'input_port_1_value': input_port_1_value, 'input_port_2': input_port_2_driver_name, 'input_port_2_value': input_port_2_value, 'input_port_3': input_port_3_driver_name, 'input_port_3_value': input_port_3_value, 'input_port_4': input_port_4_driver_name, 'input_port_4_value': input_port_4_value, 'output_port_a': output_port_a_driver_name, 'output_port_a_value': output_port_a_value, 'output_port_b': output_port_b_driver_name, 'output_port_b_value': output_port_b_value, 'output_port_c': output_port_c_driver_name, 'output_port_c_value': output_port_c_value, 'output_port_d': output_port_d_driver_name, 'output_port_d_value': output_port_d_value})
    print('Status code: ' + str(x.status_code))
    x = x.json()

    if (LegoPort('outA').status == 'no-motor'):
        a = ''
    else:
        if (x["output_port_a_state"] == 1):
            Motor('outA').on(speed=(x["output_port_a_power"]))
        else:
            Motor('outA').off()
    
    if (LegoPort('outB').status == 'no-motor'):
        a = ''
    else:
        if (x["output_port_b_state"] == 1):
            Motor('outB').on(speed=(x["output_port_b_power"]))
        else:
            Motor('outB').off()

    if (LegoPort('outC').status == 'no-motor'):
        a = ''
    else:
        if (x["output_port_c_state"] == 1):
            Motor('outC').on(speed=(x["output_port_c_power"]))
        else:
            Motor('outC').off()

    if (LegoPort('outD').status == 'no-motor'):
        a = ''
    else:
        if (x["output_port_d_state"] == 1):
            Motor('outD').on(speed=(x["output_port_d_power"]))
        else:
            Motor('outD').off()