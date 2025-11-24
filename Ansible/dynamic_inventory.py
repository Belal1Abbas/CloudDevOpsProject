#!/usr/bin/env python3
import json

inventory = {
    "all": {
        "hosts": ["192.168.214.132"],
        "vars": {
            "ansible_user": "belal",
            "ansible_ssh_private_key_file": "/home/belal/.ssh/ansible_id_ed25519"
        }
    }
}

print(json.dumps(inventory))

