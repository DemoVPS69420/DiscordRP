def start_script(script_path):
    import subprocess
    process = subprocess.Popen(['python', script_path])
    return process

def stop_script(process):
    if process:
        process.terminate()
        process.wait()

def is_running(process):
    return process.poll() is None if process else False