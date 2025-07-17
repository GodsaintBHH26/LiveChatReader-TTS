from chatLoader import chatReader

if __name__ == '__main__':
    print("Youtube Live Chat reader:")
    live_id = input("Enter the live stream ID: ").strip()
    chatReader(live_id)