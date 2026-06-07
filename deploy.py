import sys
import json
import os
from datetime import datetime

def main():
    # FR-DEP-01: Accept a command-line target environment argument
    if len(sys.argv) < 2:
        print("Error: Target environment argument is required. Usage: python deploy.py <environment>")
        sys.exit(1)
        
    target_env = sys.argv[1].lower()
    
    # FR-DEP-02: Construct a configuration object for the selected environment
    if target_env == "test":
        config = {
            "model_threshold": 0.7,
            "faq_confidence": 0.60,
            "debug": False
        }
    elif target_env == "dev":
        config = {
            "model_threshold": 0.5,
            "faq_confidence": 0.20,
            "debug": True
        }
    else:
        config = {
            "model_threshold": 0.6,
            "faq_confidence": 0.40,
            "debug": False
        }
        
    deployment_data = {
        "environment": target_env,
        "status": "success",
        "deployed_at": datetime.utcnow().isoformat() + "Z",
        "config": config
    }
    
    # FR-DEP-03: Write deployment output to a JSON file named according to the target environment
    filename = f"deployed_{target_env}.json"
    
    try:
        with open(filename, "w") as f:
            json.dump(deployment_data, f, indent=4)
        
        # FR-DEP-04: Print deployment details to the console
        print(f"\n========================================")
        print(f"Deployment SUCCESS")
        print(f"Target Environment: {target_env.upper()}")
        print(f"Deployment Receipt: {filename}")
        print(f"Details:")
        print(json.dumps(deployment_data, indent=4))
        print(f"========================================\n")
    except Exception as e:
        print(f"Error writing deployment receipt: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
