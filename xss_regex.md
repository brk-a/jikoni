# detect XSS strings using regex
### look for HTML
* sample HTML

    ```html
        <script type="text/javascript">
            let i = 10;
            console.info(i);
        </script>
    ```

* pattern
    1. angle brackets that:
        * occur in pairs: an opening and a closing one
        * may or may not contain a forward slash
        * contain text (alphabets, not numbers)
    2. alphanumeric text between two pairs of said angle brackets
* regex (JS style)

    ```javascript
        /((\%3C)|(\%253C)|<)((|%2F)|(\%252F)|\/)*[a-zA-Z0-9\%]+((\%3E)|(\%253E)|>)/ix
    ```

* `/((\%3C)|(\%253C)|<)` &rarr; opening angle bracket, `<`, using its hex, double-encoded hex and plain-text variations
* `((|%2F)|(\%252F)|\/)` &rarr; forward slash, `/`, using its hex, double-encoded hex and plain-text variations
* `/((\%3C)|(\%253C)|<)((|%2F)|(\%252F)|\/)*` &rarr; an opening angle bracket and zero or more forward slashes, `</`, using their hex, double-encoded hex and plain-text variations
* `[a-zA-Z0-9\%]+` &rarr; one or more alphanumeric characters, both upper and lower-case
* `((\%3E)|(\%253E)|>)` &rarr; closing angle bracket, `>`, using its hex, double-encoded hex and plaintext variations
* `ix` &rarr; `i`gnore case and `x`-something

### look for `img<src=` style XSS

    ```javascript
        /((\%3C)|<)((\%69)|i|(\%49))((\%6D)|m|(\%4D))((\%67|g|\%47))[^\n]+((\%3E|>))/l
    ```

### look for HTML tag-based XSS

    ```javascript
        /(javascript|vbscript|script|embed|object|iframe|frameset)/i
    ```

### look for all XSS attempts

    ```javascript
        /((\%3C|<)[^\n]+)((\%3E)|>)/l
    ```
