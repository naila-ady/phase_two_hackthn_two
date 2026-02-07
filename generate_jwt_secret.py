#!/usr/bin/env python3
"""
JWT Secret Generator
This script generates a secure JWT secret key for your application.
"""

import secrets
import string
import argparse


def generate_jwt_secret(length=32):
    """
    Generate a secure JWT secret using cryptographically secure random generation.

    Args:
        length (int): Length of the secret in bytes (default 32)

    Returns:
        str: A URL-safe base64-encoded secret string
    """
    # Generate a random URL-safe token
    secret = secrets.token_urlsafe(length)
    return secret


def main():
    parser = argparse.ArgumentParser(description='Generate a secure JWT secret key')
    parser.add_argument('--length', type=int, default=32,
                       help='Length of the secret in bytes (default: 32)')
    parser.add_argument('--hex', action='store_true',
                       help='Generate hexadecimal secret instead of URL-safe')

    args = parser.parse_args()

    if args.hex:
        # Generate hex representation
        secret = secrets.token_hex(args.length)
        print(f"JWT Secret (hex): {secret}")
        print(f"Length: {len(secret)} characters")
    else:
        # Generate URL-safe base64 representation
        secret = generate_jwt_secret(args.length)
        print(f"JWT Secret: {secret}")
        print(f"Length: {len(secret)} characters")

    print("\nTo use this secret:")
    print("1. Copy the secret above")
    print("2. Add it to your .env file as JWT_SECRET_KEY=your_secret_here")
    print("3. Make sure to keep it secure and do not commit to version control")


if __name__ == "__main__":
    main()