# android nine-dot pattern
## WTF is the android nine-dot pattern?

## can it be replicated?
To replicate Android's screen-unlock pattern hash, you need to understand how Android stores the pattern. It uses a secure hashing method, typically involving the following steps:

### Steps:
1. **User Input (Pattern Drawn)**: The user draws a pattern on the lock screen by connecting dots on a grid.
2. **Convert to a String**: The pattern is converted into a string of dot positions. For example, if the pattern starts at dot 1, then moves to dot 2, and so on, you might get something like `"1234"`.
3. **Hashing the Pattern**: Android hashes this string using a hashing algorithm (typically SHA-1 or similar). This hash is then used for authentication.
4. **Salt**: Android applies a salt to the pattern hash to further secure it. A salt is a random string or number added to the input before hashing, ensuring that the same pattern doesn't generate the same hash for different users.
5. **Secure Storage**: The final hash (often a SHA-1 or PBKDF2) is securely stored in the system’s storage.

### Code:
You can replicate the pattern hashing process using SHA-1 or SHA-256, for example, along with a salt.

Simplified example using Go:

```go
import (
	"crypto/sha1"
	"crypto/rand"
	"crypto/hmac"
	"fmt"
	"golang.org/x/crypto/pbkdf2"
	"encoding/base64"
	"strings"
)

func generateSalt() string {
	// Generate a random 16-byte salt
	salt := make([]byte, 16)
	_, err := rand.Read(salt)
	if err != nil {
		panic(err)
	}
	return base64.StdEncoding.EncodeToString(salt)
}

func hashPattern(pattern string, salt string) string {
	// Convert pattern to string if not already
	pattern = strings.Join(strings.Split(pattern, ""), "")

	// Apply SHA-1 or PBKDF2 for pattern hashing
	key := []byte(pattern)
	saltBytes := []byte(salt)
	// Using PBKDF2 for secure hashing
	hash := pbkdf2.Key(key, saltBytes, 1000, 32, sha1.New)

	return base64.StdEncoding.EncodeToString(hash)
}

func main() {
	pattern := "1234" // The pattern drawn by the user
	salt := generateSalt()

	// Hash the pattern with the generated salt
	hashedPattern := hashPattern(pattern, salt)

	fmt.Println("Salt:", salt)
	fmt.Println("Hashed Pattern:", hashedPattern)
}
```

### Explanation:
- `generateSalt()` creates a random salt.
- `hashPattern()` takes the pattern and salt, hashes them using PBKDF2 (with SHA-1), and returns the resulting hash.

This is a simplified approach, and Android’s actual implementation might differ, especially around how it handles salt, key stretching, and other security mechanisms.

### Key Points:
- Android uses SHA-1 or SHA-256 with salts.
- It’s important to use key stretching methods like PBKDF2 for added security.
- The salt is essential for preventing precomputed attacks like rainbow tables.

## how TF do I authenticate the pattern?
### 1. **Authenticating the Pattern**

To authenticate a user’s unlock pattern, you will need to:

- **Retrieve the stored hash** (from the device storage or server).
- **Apply the same hashing process** to the entered pattern using the same salt.
- **Compare the hashes**. If they match, the user is authenticated.

Here’s how you might authenticate the pattern in Go:

```go
import (
	"crypto/sha1"
	"golang.org/x/crypto/pbkdf2"
	"fmt"
	"strings"
	"encoding/base64"
)

func authenticatePattern(storedHash string, enteredPattern string, salt string) bool {
	// Hash the entered pattern with the salt
	enteredHash := hashPattern(enteredPattern, salt)

	// Compare the entered hash with the stored hash
	return storedHash == enteredHash
}

func hashPattern(pattern string, salt string) string {
	pattern = strings.Join(strings.Split(pattern, ""), "")
	key := []byte(pattern)
	saltBytes := []byte(salt)

	// Using PBKDF2 for secure hashing
	hash := pbkdf2.Key(key, saltBytes, 1000, 32, sha1.New)

	return base64.StdEncoding.EncodeToString(hash)
}

func main() {
	// Example data
	storedHash := "storedPatternHash" // Replace with the actual stored hash
	enteredPattern := "1234"          // Pattern entered by the user
	salt := "someSalt"                // Salt used for hashing

	// Authenticate the entered pattern
	if authenticatePattern(storedHash, enteredPattern, salt) {
		fmt.Println("Pattern authenticated successfully.")
	} else {
		fmt.Println("Pattern authentication failed.")
	}
}
```

### 2. **How PBKDF2 Works**

PBKDF2 (Password-Based Key Derivation Function 2) is a cryptographic algorithm used to derive a secure key from a password (or in this case, a pattern). Here’s how it works:

- **Input**: It takes a password (the unlock pattern) and a salt (a random value to prevent rainbow table attacks).
- **Iterations**: It performs multiple iterations of a cryptographic hash function (like SHA-1 or SHA-256). The more iterations, the harder it becomes to brute-force.
- **Output**: It produces a fixed-length output (e.g., a 256-bit key), which is used for further authentication or encryption.

In essence, PBKDF2 makes brute-forcing more difficult by applying a hash function multiple times (key stretching).

### 3. **PBKDF2 Vulnerabilities**

While PBKDF2 is considered a strong algorithm, it has some limitations and vulnerabilities:

- **Parallelization**: PBKDF2 is vulnerable to parallelized brute-force attacks if not configured with enough iterations. Attackers can use GPUs or specialised hardware to speed up the process.
- **Salt Management**: If the salt is predictable or too short, it reduces the effectiveness of the PBKDF2 algorithm. Salt must be sufficiently random and long to ensure security.
- **Algorithm Strength**: As computing power increases, PBKDF2's strength may degrade if the iteration count isn't increased to compensate.

That said, PBKDF2 is still one of the most widely used and recommended key derivation functions, especially when paired with high iteration counts.

### 4. **Can You Decrypt the Pattern?**

You **cannot decrypt** the pattern directly if you have access to the hash. The hash is a one-way transformation, meaning you can’t reverse it to get the original input (pattern). This is the principle behind secure hashing algorithms.

However, if you can find the salt and the hash (and have enough time), you could try to **brute-force** the original pattern by hashing possible patterns and comparing them to the stored hash. This is computationally expensive, and without knowing the salt or having a weak pattern, it can be very difficult.

### 5. **Where is the Hash Stored on an Android Device?**

The hash and salt for the screen unlock pattern are typically stored in Android’s **Keystore** system, which provides secure storage for cryptographic keys. The specific location varies based on the Android version and device, but generally:

- **Android 4.3 (Jelly Bean) and later**: The pattern hash and salt are stored in a **secure location** in the system partition, within the **Keystore** or **SharedPreferences** (depending on the device configuration).
- **System Files**: In older versions, these might be stored in files like `/data/system/gesture.key` or `/data/system/password.key` (though this is not guaranteed across devices).

Access to these files typically requires root access to the device or bypassing Android’s security mechanisms, which are designed to prevent unauthorized access to sensitive data like the pattern hash.

#### Example of Where to Look for Stored Hash:
- **Location**: `/data/system/gesture.key` (may vary by device and Android version).
  
You can try looking for this file if you have root access on the device. If you find it, you might see the encrypted pattern hash and salt.

### Key points:
- Authenticating the pattern involves comparing the stored hash with the hashed version of the entered pattern.
- PBKDF2 makes brute-forcing more difficult through iterations and key stretching.
- The hash can’t be decrypted, but brute-forcing it is possible if you can access the salt and hash.
- The hash is stored securely within Android’s Keystore system, and its location can depend on the Android version and device.
