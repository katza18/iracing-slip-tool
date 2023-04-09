import pyirsdk as irsdk

def calculate_slip_angle(telemetry):
    # Get driver telemetry variables
    velocity_x = telemetry['VelocityX']
    velocity_y = telemetry['VelocityY']
    yaw_rate = telemetry['YawRate']
    steer_angle = telemetry['SteeringWheelAngle']
    lateral_accel = telemetry['LateralAcceleration']

    # Calculate slip angle using the equation
    if velocity_x != 0:
        slip_angle = (steer_angle - (yaw_rate * (0.5 * (2 * abs(velocity_y) / velocity_x)))) - (180 / 3.14159 * lateral_accel * 1.2)
    else:
        slip_angle = 0

    return slip_angle
