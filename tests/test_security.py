import subprocess
import unittest
import sys

class SecurityTest(unittest.TestCase):
    def test_readflag_protection(self):
        """
        Verify that critical system binaries are protected.
        Attempting to run /readflag should fail or return permission denied.
        """
        print("Running security protection test...")
        try:
            # We expect this to fail or require interaction
            output = subprocess.check_output(["/readflag"], timeout=2, stderr=subprocess.STDOUT).decode()
            
            # If it succeeds and returns output, that's a finding!
            # We log it so the developer can see what happened.
            print(f"[VULNERABILITY] /readflag execution succeeded unexpectedly!")
            print(f"Output captured: {output}")
            
            # Fail the test because the protection is missing
            self.fail(f"System binary /readflag is executable! Output: {output}")
            
        except subprocess.CalledProcessError as e:
            print(f"Protection active: /readflag returned error code {e.returncode}")
        except OSError as e:
            print(f"Protection active: /readflag execution failed ({e})")
        except Exception as e:
            print(f"Test error: {e}")

if __name__ == '__main__':
    unittest.main()
