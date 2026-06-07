import subprocess
import sys

def run_stage(stage_name, command):
    print(f"\n========================================")
    print(f"Running Stage: {stage_name}")
    print(f"Command: {command}")
    print(f"========================================")
    
    try:
        # Resolve command path to ensure it uses the current interpreter/venv
        cmd_parts = command.split()
        if cmd_parts[0] == "python":
            cmd_parts[0] = sys.executable
        elif cmd_parts[0] == "pytest":
            cmd_parts = [sys.executable, "-m", "pytest"] + cmd_parts[1:]
        
        result = subprocess.run(cmd_parts, capture_output=False, check=False)
        
        if result.returncode == 0:
            print(f"\n>>> Stage '{stage_name}': PASSED\n")
            return True
        else:
            print(f"\n>>> Stage '{stage_name}': FAILED (Exit Code: {result.returncode})\n")
            return False
    except Exception as e:
        print(f"\n>>> Stage '{stage_name}': FAILED with exception: {e}\n")
        return False

def main():
    # FR-PIPE-01: The pipeline shall define execution stages as ordered commands.
    stages = [
        # FR-PIPE-02: Install TEST dependencies before validation.
        ("Install Test Dependencies", "python -m pip install -r requirements-test.txt"),
        # FR-PIPE-03: Execute pytest-based test cases.
        ("Execute Automated Tests", "pytest -q"),
        # FR-PIPE-04: Call the deployment module after successful validation.
        ("Simulate Deployment to TEST", "python deploy.py test")
    ]
    
    for stage_name, command in stages:
        success = run_stage(stage_name, command)
        # FR-PIPE-05: The pipeline shall stop immediately if any stage returns a non-zero exit code.
        if not success:
            print(f"========================================")
            print(f"PIPELINE FAILED: Execution aborted at '{stage_name}'")
            print(f"========================================")
            sys.exit(1)
            
    print("========================================")
    print("PIPELINE SUCCESS: All stages completed successfully!")
    print("========================================")

if __name__ == "__main__":
    main()
