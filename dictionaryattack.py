import hashlib
import time


def hash_password(password: str, algorithm: str = "sha256") -> str:
    h = hashlib.new(algorithm)
    h.update(password.encode("utf-8"))
    return h.hexdigest()


def dictionary_attack(target_hash: str, wordlist: list, algorithm: str = "sha256"):
    
    start = time.perf_counter()
    attempts = 0

    for word in wordlist:
        attempts += 1
        candidate_hash = hash_password(word, algorithm)
        if candidate_hash == target_hash:
            elapsed = time.perf_counter() - start
            return {
                "found": True,
                "password": word,
                "attempts": attempts,
                "time_seconds": elapsed,
            }

    elapsed = time.perf_counter() - start
    return {
        "found": False,
        "password": None,
        "attempts": attempts,
        "time_seconds": elapsed,
    }


if __name__ == "__main__":
    
    test_password = "password123"
    target_hash = hash_password(test_password)

    print(f"(SHA-256): {target_hash}")

    dictionary = [
        "123456", "password", "admin", "welcome",
        "password123", "letmein", "qwerty", "iloveyou",
    ]

    result = dictionary_attack(target_hash, dictionary)

    if result["found"]:
        print(f"Password found: '{result['password']}' in {result['attempts']} attempts "
              f"({result['time_seconds']*1000:.3f} ms)")
    else:
        print(f"Password not found after {result['attempts']} attempts "
              f"({result['time_seconds']*1000:.3f} ms)")
