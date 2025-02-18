package main

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

// func hashPattern(pattern string, salt string) string {
// 	pattern = strings.Join(strings.Split(pattern, ""), "")
// 	key := []byte(pattern)
// 	saltBytes := []byte(salt)

// 	// Using PBKDF2 for secure hashing
// 	hash := pbkdf2.Key(key, saltBytes, 1000, 32, sha1.New)

// 	return base64.StdEncoding.EncodeToString(hash)
// }

func authenticate() {
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
