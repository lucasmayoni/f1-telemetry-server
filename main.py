from telemetry_f1_2021.listener import TelemetryListener

def read_from_json():


def main():
    listener = TelemetryListener(port=20777, host='')
    try:
        while True:
            packet = listener.get()
            print("RPM: %s", packet.get("m_engine_rpm") + "\n")
    except KeyboardInterrupt:
        print('Stop the car, stop the car Checo.')
        print('Stop the car, stop at pit exit.')
        print('Just pull over to the side.')


if __name__ == "__main__":
    main()
