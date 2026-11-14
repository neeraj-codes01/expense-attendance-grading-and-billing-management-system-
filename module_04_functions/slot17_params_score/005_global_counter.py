call_count=0
def track_call():
    global call_count
    call_count=call_count+1
    print("called",call_count,"times")

track_call()
track_call()
track_call()
