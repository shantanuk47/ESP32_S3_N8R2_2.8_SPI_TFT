#============================================================
# File    : generate_version.py
# Author  : Shantanu Kumar
# GitHub  : https://github.com/shantanuk47
#
# Purpose :
#   PlatformIO pre-build script that automatically generates
#   firmware version metadata using Git tags.
#
#   The script executes:
#       git describe --tags --always --dirty
#
#   and generates the file:
#       include/version.h
#
#   The generated header contains:
#       FW_VERSION
#       FW_BUILD_DATE
#       FW_BUILD_TIME
#
#   This enables firmware traceability and reproducible builds
#   across embedded projects.
#
#   This script is designed to be reused across repositories.
#============================================================

Import("env")

import subprocess
from datetime import datetime


def get_git_version():
    try:
        version = subprocess.check_output(
            ["git", "describe", "--tags", "--always", "--dirty"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except Exception:
        version = "unknown"

    return version


version = get_git_version()
now = datetime.now()

header_content = f"""
/* Auto-generated file. DO NOT EDIT */

#ifndef FW_VERSION_H
#define FW_VERSION_H

#define FW_VERSION "{version}"
#define FW_BUILD_DATE "{now.strftime('%Y-%m-%d')}"
#define FW_BUILD_TIME "{now.strftime('%H:%M:%S')}"

#endif
"""

with open("include/version.h", "w") as f:
    f.write(header_content)