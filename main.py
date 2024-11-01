#!/usr/bin/env python3

import platform
import sys
from datetime import datetime
from typing import Dict

class SystemInfo:
    @staticmethod
    def get_info() -> Dict[str, str]:
        return {
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "timestamp": datetime.now().isoformat(),
            "implementation": platform.python_implementation()
        }

    @staticmethod
    def display_info() -> None:
        info = SystemInfo.get_info()
        print("\n=== Python Environment Info ===")
        for key, value in info.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        print("============================\n")

def main() -> None:
    try:
        SystemInfo.display_info()
        
        # Interactive demo
        name = input("Enter your name (or press Enter to skip): ").strip()
        if name:
            print(f"\nHello, {name}! Welcome to Python in WebContainers! 🚀")
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()