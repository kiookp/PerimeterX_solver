import base64
import re
import sys


def ob_decrypt(encoded_str: str, key: int = 39) -> str:
    invalid_base64_pattern = r'[^+/=0-9A-Za-z]'
    invalid_padding_pattern = r'=[^=]|={3}'

    try:
        if re.search(invalid_base64_pattern, encoded_str) or (
                '=' in encoded_str and (
                re.search(invalid_padding_pattern, encoded_str)
        )
        ):
            print(f"❌ Invalid Base64 format: {encoded_str}", file=sys.stderr)
            return None

        padding_needed = (4 - len(encoded_str) % 4) % 4
        encoded_str_padded = encoded_str + '=' * padding_needed

        raw = base64.b64decode(encoded_str_padded)

        decrypted = ''.join(chr(b ^ key) for b in raw)

        return decrypted

    except Exception as e:
        print(f"❌ Decryption error: {e}", file=sys.stderr)
        return None


def main():
    if len(sys.argv) > 1:
        encoded = sys.argv[1]
    else:
        encoded = input("请输入加密后的 Base64+XOR 字符串：").strip()

    if not encoded:
        print("⚠️ 输入不能为空！", file=sys.stderr)
        sys.exit(1)

    key = 39
    result = ob_decrypt(encoded, key)

    if result:
        print(f"\n--- Decrypted Result ---")
        print(result)
    else:
        print("❌ Decryption failed", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
