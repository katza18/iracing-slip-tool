import irsdk

def calculate_slip_angle(data):
    # Get driver telemetry variables
    velocity_x = data['VelocityX']
    velocity_y = data['VelocityY']
    yaw_rate = data['YawRate']
    steer_angle = data['SteeringWheelAngle']
    lateral_accel = data['LateralAcceleration']

    # Calculate slip angle using the equation
    if velocity_x != 0:
        slip_angle = (steer_angle - (yaw_rate * (0.5 * (2 * abs(velocity_y) / velocity_x)))) - (180 / 3.14159 * lateral_accel * 1.2)
    else:
        slip_angle = 0

    return slip_angle


def main():
    ir = irsdk.IRSDK()
    ir.startup()

    while True:
        if ir.is_initialized() and ir.is_connected():
            # Check if car is on track
            if ir['IsOnTrack'] == 1:
                data = ir.get_session_data()
                slip_angle = iracing_slip_tool.calculate_slip_angle(data)

                # Display slip angle
                print(f"Slip Angle: {slip_angle:.2f} degrees")

        # Sleep to avoid overloading the CPU
        time.sleep(0.05)

    ir.shutdown()

if __name__ == '__main__':
    main()
