package main

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
